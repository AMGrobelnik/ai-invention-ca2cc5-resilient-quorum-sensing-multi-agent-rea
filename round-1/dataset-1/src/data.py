# /// script
# dependencies = ["datasets", "jsonschema"]
# ///
import os
import json
from datasets import load_dataset

WORKSPACE = "/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"

def synonym_replace(text):
    synonyms = {
        "calculate": "compute",
        "find": "determine",
        "how many": "what quantity of",
        "total": "combined sum",
        "cost": "price",
        "sold": "disposed of",
        "bought": "purchased",
        "left": "remaining",
        "each": "every single",
        "start": "begin",
        "write": "implement",
        "function": "routine",
        "return": "output",
        "given": "provided",
        "list": "array",
        "string": "text sequence"
    }
    words = text.split()
    new_words = []
    for w in words:
        w_lower = w.lower().strip(".,?!")
        if w_lower in synonyms:
            rep = synonyms[w_lower]
            if w.isupper():
                rep = rep.upper()
            elif w[0].isupper():
                rep = rep.capitalize()
            new_words.append(rep)
        else:
            new_words.append(w)
    return " ".join(new_words)

def generate_paraphrases(text):
    p1 = synonym_replace(text)
    p2 = f"Assuming the following scenario: {text}. Determine the exact solution."
    p3 = f"Please solve this problem step by step: {text}"
    return [p1, p2, p3]

def main():
    print("Loading the 2 chosen datasets (GSM8K and MBPP)...")
    try:
        gsm8k_raw = load_dataset("openai/gsm8k", "main", split="test", streaming=True)
        gsm8k_items = list(gsm8k_raw.take(50))
    except Exception:
        gsm8k_items = []

    try:
        mbpp_raw = load_dataset("google-research-datasets/mbpp", "full", split="test", streaming=True)
        mbpp_items = list(mbpp_raw.take(50))
    except Exception:
        mbpp_items = []

    datasets_list = []

    def process_items(items, dataset_name):
        examples = []
        for idx, item in enumerate(items):
            q = item.get("question", item.get("text", ""))
            ans = item.get("answer", item.get("code", ""))
            if not q:
                continue
            paraphrases = generate_paraphrases(q)
            ex = {
                "input": q,
                "output": str(ans),
                "metadata_fold": 0,
                "metadata_row_index": idx,
                "metadata_category": "math_or_code",
                "metadata_difficulty": "medium",
                "metadata_paraphrase_1": paraphrases[0],
                "metadata_paraphrase_2": paraphrases[1],
                "metadata_paraphrase_3": paraphrases[2]
            }
            examples.append(ex)
        if examples:
            datasets_list.append({
                "dataset": dataset_name,
                "examples": examples
            })

    process_items(gsm8k_items, "gsm8k")
    process_items(mbpp_items, "mbpp")

    output_data = {
        "datasets": datasets_list
    }

    out_path = os.path.join(WORKSPACE, "full_data_out.json")
    with open(out_path, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"Saved 2 datasets to {out_path}")

if __name__ == "__main__":
    main()
