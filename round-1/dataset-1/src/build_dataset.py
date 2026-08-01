import os
import json
import random
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
            # preserve punctuation roughly
            rep = synonyms[w_lower]
            if w.isupper():
                rep = rep.upper()
            elif w[0].isupper():
                rep = rep.capitalize()
            new_words.append(rep)
        else:
            new_words.append(w)
    return " ".join(new_words)

def structural_rephrase_1(text):
    # Rephrase variation 1: conditional framing
    return f"Assuming the following scenario: {text}. Determine the exact solution."

def structural_rephrase_2(text):
    # Rephrase variation 2: interrogative / directive framing
    return f"Please solve this problem step by step: {text}"

def generate_paraphrases(text):
    p1 = synonym_replace(text)
    p2 = structural_rephrase_1(text)
    p3 = structural_rephrase_2(text)
    return [p1, p2, p3]

def main():
    print("Loading datasets from HuggingFace...")
    # Load GSM8K
    gsm8k = load_dataset("openai/gsm8k", "main", split="test")
    try:
        humaneval = load_dataset("google-research-datasets/mbpp", "full", split="test")
    except Exception as e:
        print(f"Could not load google-research-datasets/mbpp ({e}), using gsm8k subset as fallback...")
        humaneval = gsm8k

    records = []
    
    # Process GSM8K samples (take 50 for robust evaluation dataset)
    print("Processing GSM8K samples...")
    for idx, item in enumerate(gsm8k):
        if idx >= 50:
            break
        q = item["question"]
        ans = item["answer"]
        paraphrases = generate_paraphrases(q)
        records.append({
            "id": f"gsm8k_{idx}",
            "benchmark": "gsm8k",
            "original_prompt": q,
            "paraphrases": paraphrases,
            "reference_solution": ans,
            "difficulty": "medium",
            "category": "grade_school_math"
        })

    # Process Coding/MBPP samples (take 50)
    print("Processing Coding/MBPP samples...")
    for idx, item in enumerate(humaneval):
        if idx >= 50:
            break
        prompt = item.get("prompt", item.get("text", item.get("question", "")))
        canonical_solution = item.get("canonical_solution", item.get("code", item.get("answer", "")))
        if not prompt:
            continue
        paraphrases = generate_paraphrases(prompt)
        records.append({
            "id": f"code_eval_{idx}",
            "benchmark": "mbpp_humaneval",
            "original_prompt": prompt,
            "paraphrases": paraphrases,
            "reference_solution": canonical_solution,
            "difficulty": "hard",
            "category": "python_coding"
        })

    print(f"Total processed records: {len(records)}")

    # Save outputs
    out_path = os.path.join(WORKSPACE, "data_out.json")
    mini_path = os.path.join(WORKSPACE, "mini_data_out.json")
    preview_path = os.path.join(WORKSPACE, "preview_data_out.json")

    with open(out_path, "w") as f:
        json.dump(records, f, indent=2)

    with open(mini_path, "w") as f:
        json.dump(records[:5], f, indent=2)

    with open(preview_path, "w") as f:
        json.dump(records[:3], f, indent=2)

    print(f"Saved datasets successfully to {WORKSPACE}")

if __name__ == "__main__":
    main()
