"""
Main entry point for dataset generation.

Responsibilities:
1. Load configuration
2. Generate ontology instances (TTL)
3. Run module pipelines
4. Combine results
5. Export datasets
"""

import pandas as pd
import yaml

# Load configuration
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

#kg = config["KG_output_path"]
KG_train = config["KG_train_path"]
KG_val = config["KG_val_path"]

#kgm = config["KGM_path"]
KGM_train = config["KGM_train_path"]
KGM_val = config["KGM_val_path"]

OUTPUT_FORMAT = config["dataset_output_format"]

# System prompt instruction
INSTRUCTION_TEXT = (
    "Generate a valid SPARQL query that includes at least the SELECT and WHERE clauses, "
    "without any prefixes or comments. All instances should use the prefix \"ex:\" "
    "(e.g., ex:FuelTank01, ex:can2, ex:L). Use descriptive notation for variables "
    "in the SPARQL triplet (e.g., ?signal, ?message, ?timestamp, ?signalValue). "
    "Ensure that the generated query is syntactically valid according to SPARQL standards."
)

# Import modules
import kg_maker as kgm
import module_a
import module_g
import module_d


def build_dataset():
    """Runs the full pipeline and returns train and validation DataFrames."""

    # Step 1: Generate train, val ontology instances
    kgm.generate_instances(KGM_train, KG_train)
    kgm.generate_instances(KGM_val, KG_val)

    # Step 2: Run module pipelines
    df_a_train, df_a_val = module_a.finall()
    df_g_train, df_g_val = module_g.finall()
    df_d_train, df_d_val = module_d.finall()

    # Step 3: Combine results
    df_train = pd.concat([df_a_train, df_g_train, df_d_train], ignore_index=True)
    df_val   = pd.concat([df_a_val, df_g_val, df_d_val], ignore_index=True)

    df_train = df_train.drop_duplicates().reset_index(drop=True)
    df_val = df_val.drop_duplicates().reset_index(drop=True)

    # Add instruction column
    #df_train.insert(0, "Instruction", INSTRUCTION_TEXT)
    #df_val.insert(0, "Instruction", INSTRUCTION_TEXT)
    
    if "Instruction" not in df_train.columns:
        df_train.insert(0, "Instruction", INSTRUCTION_TEXT)

    if "Instruction" not in df_val.columns:
        df_val.insert(0, "Instruction", INSTRUCTION_TEXT)

    return df_train, df_val


# Save datasets
def save_dataset(df_train, df_val):
    """Exports train and validation datasets."""

    if OUTPUT_FORMAT == "csv":
        df_train.to_csv("final_dataset_train.csv", index=False)
        df_val.to_csv("final_dataset_val.csv", index=False)

    elif OUTPUT_FORMAT == "json":
        df_train.to_json("final_dataset_train.json", orient="records", lines=True)
        df_val.to_json("final_dataset_val.json", orient="records", lines=True)

    else:
        print("Invalid dataset_output_format in config.yaml")


def main():
    df_train, df_val = build_dataset()
    save_dataset(df_train, df_val)

    print("Train dataset:")
    print(df_train)

    print("\nValidation dataset:")
    print(df_val)

if __name__ == "__main__":
    main()
