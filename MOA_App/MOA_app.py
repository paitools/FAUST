import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import requests
import ollama


ONTOP_ENDPOINT = "http://localhost:8080/sparql"
GGUF_LLM = "dbc_model"


# =========================================================
# LAYER 2 — LLM TRANSLATOR (NL → SPARQL)
# =========================================================
class LLMTranslator:
    def __init__(self, model=GGUF_LLM):
        self.model = model

    def generate_query(self, text):
        response = ollama.chat(
            model=self.model,
            messages=[{'role': 'user', 'content': text}]
        )

        content = response['message']['content']

        start = content.upper().find("SELECT")
        end = content.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("Could not extract SPARQL query")

        return content[start:end + 1].strip()


# =========================================================
# LAYER 4 — OBDA ENGINE (ONTOP CLIENT)
# =========================================================
class OntopClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def execute_query(self, query):
        try:
            response = requests.post(
                self.endpoint,
                data={"query": query},
                headers={"Accept": "application/sparql-results+json"}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print("Ontop error:", e)
            return None


# =========================================================
# LAYER 3 — PROCESSING UNIT
# (Query Processing + Output Formatting)
# =========================================================
class QueryProcessor:
    def __init__(self, prefix_map):
        self.prefix_map = prefix_map

        self.prefixes = "\n".join(
            f"PREFIX {v} <{k}>" for k, v in prefix_map.items()
        ) + "\n"

    # ---------- PART 1: QUERY PROCESSING ----------
    def prepare_query(self, raw_query):
        return self.prefixes + raw_query

    # ---------- PART 2: OUTPUT FORMATTING ----------
    def shorten_uri(self, uri):
        for full, prefix in self.prefix_map.items():
            if uri.startswith(full):
                return uri.replace(full, prefix)
        return uri

    def format_results(self, results):
        if not results:
            return [], []

        vars_ = results.get("head", {}).get("vars", [])
        bindings = results.get("results", {}).get("bindings", [])

        rows = []
        for row in bindings:
            values = []
            for var in vars_:
                if var in row:
                    val = self.shorten_uri(row[var]["value"])
                else:
                    val = ""
                values.append(val)
            rows.append(values)

        return vars_, rows


# =========================================================
# LAYER 1 — USER INPUT (UI)
# =========================================================
class GUIApp:
    def __init__(self, root):

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("paitools")
        self.root.geometry("800x600")

        # ---------------- MODULE INIT ----------------
        self.prefix_map = {
            "http://example.org/individuals#": "ex:",
            "http://www.w3.org/2002/07/owl#": "owl:",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf:",
            "http://www.w3.org/2000/01/rdf-schema#": "rdfs:",
            "http://www.w3.org/2001/XMLSchema#": "xsd:",
            "http://purl.org/dc/terms/": "dct:",
            "http://xmlns.com/foaf/0.1/": "foaf:",
            "http://purl.org/ontology/bibo/": "bibo:",
            "http://www.w3.org/ns/sosa/": "sosa:",
            "http://www.w3.org/ns/ssn/": "ssn:",
            "http://qudt.org/schema/qudt/": "qudt:",
            "http://qudt.org/vocab/unit/": "unit:",
            "https://paitools.github.io/DBCOntology/DBC.owl#": "dbc:"
        }

        self.translator = LLMTranslator()
        self.processor = QueryProcessor(self.prefix_map)
        self.ontop = OntopClient(ONTOP_ENDPOINT)

        # ---------------- UI ----------------
        ctk.CTkLabel(
            root,
            text="MOA",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.input_frame = ctk.CTkFrame(root, corner_radius=15)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.input_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Ask your question...",
            height=40,
            border_width=0,
            corner_radius=25
        )
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(15, 5), pady=10)

        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="➤",
            width=40,
            height=40,
            corner_radius=20,
            fg_color="white",
            hover_color="gray",
            text_color="black",
            command=self.send_input
        )
        self.send_button.pack(side="right", padx=(5, 15), pady=10)

        # QUERY BOX
        ctk.CTkLabel(root, text="Generated Query",
                     font=ctk.CTkFont(size=14, weight="bold")
                     ).pack(anchor="w", padx=20)

        self.response_entry = ctk.CTkTextbox(root, height=120)
        self.response_entry.pack(padx=20, pady=10, fill="x")

        # RESULTS
        ctk.CTkLabel(root, text="Results",
                     font=ctk.CTkFont(size=14, weight="bold")
                     ).pack(anchor="w", padx=20)

        self.tree_frame = ctk.CTkFrame(root)
        self.tree_frame.pack(padx=20, pady=10, expand=True, fill="both")

        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(expand=True, fill="both")

    # ---------------------------------------------------------
    def send_input(self):

        user_text = self.input_entry.get().strip()
        if not user_text:
            return

        self.response_entry.delete("1.0", tk.END)

        try:
            # 1. NL → SPARQL
            query = self.translator.generate_query(user_text)

            # 2. Processing (prefixes)
            full_query = self.processor.prepare_query(query)

            # 3. OBDA execution
            results = self.ontop.execute_query(full_query)

            # 4. Format results
            cols, rows = self.processor.format_results(results)

        except Exception as e:
            self.response_entry.insert("1.0", str(e))
            return

        self.response_entry.insert("1.0", query)

        self.display_table(cols, rows)

    # ---------------------------------------------------------
    def display_table(self, columns, rows):

        self.tree.delete(*self.tree.get_children())

        if not columns:
            return

        self.tree["columns"] = columns
        self.tree["show"] = "headings"

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for row in rows:
            self.tree.insert("", tk.END, values=row)


# =========================================================
# MAIN
# =========================================================
if __name__ == "__main__":
    root = ctk.CTk()
    app = GUIApp(root)
    root.mainloop()
