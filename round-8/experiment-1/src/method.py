import os
import json
import numpy as np
import gc

WORKSPACE = "/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_8/gen_art/gen_art_experiment_1"

def generate_synthetic_series(num_steps=200, seed=42):
    np.random.seed(seed)
    t = np.arange(num_steps)
    base = np.sin(2 * np.pi * t / 50.0) * 10.0
    steps = np.zeros(num_steps)
    if num_steps >= 50:
        steps[50:120] = 15.0
    if num_steps >= 120:
        steps[120:180] = -10.0
    
    noise = np.random.normal(0, 1.5, size=num_steps)
    series = base + steps + noise
    return series

def naive_persistence(series):
    preds = np.roll(series, 1)
    preds[0] = series[0]
    return preds

def moving_average_3(series):
    preds = np.zeros_like(series)
    for t in range(len(series)):
        if t == 0:
            preds[t] = series[0]
        elif t == 1:
            preds[t] = series[0]
        elif t == 2:
            preds[t] = (series[0] + series[1]) / 2.0
        else:
            preds[t] = (series[t-1] + series[t-2] + series[t-3]) / 3.0
    return preds

def exponential_weighted_moving_average(series, alpha=0.4):
    preds = np.zeros_like(series)
    curr = series[0]
    for t in range(len(series)):
        if t == 0:
            preds[t] = series[0]
        else:
            curr = alpha * series[t-1] + (1 - alpha) * curr
            preds[t] = curr
    return preds

def run_experiment():
    seeds = [42, 123, 456, 789, 1011]
    synthetic_examples = []
    
    all_naive_mse = []
    all_ma3_mse = []
    all_ewma_mse = []
    all_naive_mae = []
    all_ma3_mae = []
    all_ewma_mae = []

    for seed in seeds:
        series = generate_synthetic_series(num_steps=200, seed=seed)
        warmup = 10
        y_true = series[warmup:]
        naive_preds = naive_persistence(series)[warmup:]
        ma3_preds = moving_average_3(series)[warmup:]
        ewma_preds = exponential_weighted_moving_average(series, alpha=0.4)[warmup:]
        
        for idx in range(len(y_true)):
            actual = float(y_true[idx])
            p_naive = float(naive_preds[idx])
            p_ma3 = float(ma3_preds[idx])
            p_ewma = float(ewma_preds[idx])
            
            err_naive_mse = (actual - p_naive) ** 2
            err_ma3_mse = (actual - p_ma3) ** 2
            err_ewma_mse = (actual - p_ewma) ** 2
            
            err_naive_mae = abs(actual - p_naive)
            err_ma3_mae = abs(actual - p_ma3)
            err_ewma_mae = abs(actual - p_ewma)
            
            all_naive_mse.append(err_naive_mse)
            all_ma3_mse.append(err_ma3_mse)
            all_ewma_mse.append(err_ewma_mse)
            all_naive_mae.append(err_naive_mae)
            all_ma3_mae.append(err_ma3_mae)
            all_ewma_mae.append(err_ewma_mae)
            
            synthetic_examples.append({
                "input": f"Synthetic time series forecast step {warmup + idx} for seed {seed}",
                "output": str(actual),
                "predict_naive": str(p_naive),
                "predict_moving_average_3": str(p_ma3),
                "predict_ewma": str(p_ewma),
                "eval_naive_mse": float(err_naive_mse),
                "eval_ma3_mse": float(err_ma3_mse),
                "eval_ewma_mse": float(err_ewma_mse),
                "metadata_seed": str(seed),
                "metadata_step": str(warmup + idx)
            })
            
        del series, y_true, naive_preds, ma3_preds, ewma_preds
        gc.collect()

    # Load dependency datasets
    dependency_datasets = []
    dep_path = "/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    if os.path.exists(dep_path):
        with open(dep_path, "r") as f:
            dep_data = json.load(f)
            if isinstance(dep_data, dict) and "datasets" in dep_data:
                dependency_datasets = dep_data["datasets"]

    datasets_output_method = [
        {
            "dataset": "synthetic_autoinducer_buffer_time_series",
            "examples": [{k: v for k, v in ex.items() if not k.startswith("eval_")} for ex in synthetic_examples]
        }
    ] + dependency_datasets

    method_out_data = {
        "metadata": {
            "title": "Moving Average vs Naive Persistence Forecasting",
            "description": "Comparison of 3-point moving average, EWMA, and naive persistence on synthetic time series with Gaussian noise."
        },
        "datasets": datasets_output_method
    }

    method_out_path = os.path.join(WORKSPACE, "method_out.json")
    with open(method_out_path, "w") as f:
        json.dump(method_out_data, f, indent=2)

    # Evaluation output with metrics_agg
    metrics_agg = {
        "naive_mse_mean": float(np.mean(all_naive_mse)),
        "ma3_mse_mean": float(np.mean(all_ma3_mse)),
        "ewma_mse_mean": float(np.mean(all_ewma_mse)),
        "naive_mae_mean": float(np.mean(all_naive_mae)),
        "ma3_mae_mean": float(np.mean(all_ma3_mae)),
        "ewma_mae_mean": float(np.mean(all_ewma_mae))
    }

    eval_datasets_output = [
        {
            "dataset": "synthetic_autoinducer_buffer_time_series",
            "examples": synthetic_examples
        }
    ]

    for dep_ds in dependency_datasets:
        dep_examples = []
        for ex in dep_ds["examples"]:
            new_ex = dict(ex)
            dep_examples.append(new_ex)
        eval_datasets_output.append({
            "dataset": dep_ds["dataset"],
            "examples": dep_examples
        })

    eval_out_data = {
        "metadata": {
            "experiment": "Moving Average vs Naive Persistence Forecasting",
            "smoke_test": False,
            "num_steps": 200
        },
        "metrics_agg": metrics_agg,
        "datasets": eval_datasets_output
    }

    eval_out_path = os.path.join(WORKSPACE, "eval_out.json")
    with open(eval_out_path, "w") as f:
        json.dump(eval_out_data, f, indent=2)

    # Generate full, mini, preview variants
    def make_variants(filepath, base_name):
        with open(filepath, "r") as f:
            data = json.load(f)
        
        full_path = os.path.join(WORKSPACE, f"full_{base_name}.json")
        with open(full_path, "w") as f:
            json.dump(data, f, indent=2)
            
        mini_data = dict(data)
        mini_datasets = []
        for ds in data["datasets"]:
            mini_ds = dict(ds)
            mini_ds["examples"] = ds["examples"][:3]
            mini_datasets.append(mini_ds)
        mini_data["datasets"] = mini_datasets
        
        mini_path = os.path.join(WORKSPACE, f"mini_{base_name}.json")
        with open(mini_path, "w") as f:
            json.dump(mini_data, f, indent=2)
            
        def truncate_recursive(obj):
            if isinstance(obj, str):
                return obj[:200] + "..." if len(obj) > 200 else obj
            elif isinstance(obj, dict):
                return {k: truncate_recursive(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [truncate_recursive(item) for item in obj]
            return obj
            
        preview_data = truncate_recursive(mini_data)
        preview_path = os.path.join(WORKSPACE, f"preview_{base_name}.json")
        with open(preview_path, "w") as f:
            json.dump(preview_data, f, indent=2)

    make_variants(method_out_path, "method_out")
    make_variants(eval_out_path, "eval_out")

    print("Successfully generated method_out.json, eval_out.json and all variants!")

if __name__ == "__main__":
    run_experiment()
