import pandas as pd
from collections import defaultdict
import yaml


# Load Configuration
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

ontology = config["ontology_path"]
prefix_line = config["prefix_line"]
inst_prefix = config["instance_prefix"]


INSTANCES_MARKER = """
#################################################################

# Ontology Instances

#################################################################

"""
def generate_instances(kgm, kg):
    # Read existing ontology
    with open(ontology, 'r', encoding='utf-8') as f:
        ontology_body = f.read()

    # Read each sheet and build TTL
    sheets = pd.read_excel(kgm, sheet_name=None)
    final_ttl = ""

    for sheet_name, df in sheets.items():
        if df.empty:
            continue

        cols = df.columns.tolist()
        if "Individual" not in cols:
            raise KeyError(f"Sheet {sheet_name!r} has no 'Individual' column")

        predicates = cols[1:]  # all columns after 'Individual'

        for _, row in df.iterrows():
            subj = str(row["Individual"]).strip()
            if not subj or pd.isna(subj):
                continue

            # Collect predicate → object list
            pmap = defaultdict(list)
            for prop in predicates:
                cell = row[prop]
                if pd.notna(cell) and str(cell).strip():
                    for raw in str(cell).split(','):
                        v = raw.strip()
                        if not v:
                            continue

                        if prop == "rdf:type":
                            pmap["a"].append(v)
                        else:
                            if v.startswith('"') or v.startswith('unit'):
                                pmap[prop].append(v)
                            else:
                                pmap[prop].append(f"{inst_prefix}:{v}")

            # Build TTL block for this subject
            final_ttl += f"{inst_prefix}:{subj} "
            triples = []
            for p, objs in pmap.items():
                objs_s = " , ".join(objs)
                triples.append(f"{p} {objs_s}")

            final_ttl += " ;\n    ".join(triples) + " .\n\n"

    # Write final TTL output
    with open(kg, 'w', encoding='utf-8') as f:
        f.write(prefix_line)
        f.write(ontology_body.rstrip() + "\n")
        f.write(INSTANCES_MARKER)
        f.write(final_ttl)

    print(f"✅ Written merged ontology + individuals to `{kg}`")
