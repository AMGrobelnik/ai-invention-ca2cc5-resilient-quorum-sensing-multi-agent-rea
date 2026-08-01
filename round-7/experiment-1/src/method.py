import numpy as np
import json
import os
import gc

def generate_synthetic_series(num_steps=1000, seed=42):
    np.random.seed(seed)
    t = np.arange(num_steps)
    base = np.sin(2 * np.pi * t / 50.0) * 10.0
    steps = np.zeros(num_steps)
    if num_steps >= 200:
        steps[200:min(400, num_steps)] = 15.0
    if num_steps >= 400:
        steps[400:min(600, num_steps)] = -10.0
    if num_steps >= 600:
        steps[600:min(800, num_steps)] = 20.0
    
    noise = np.random.normal(0, 2.0, size=num_steps)
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
    
    for seed in seeds:
        series = generate_synthetic_series(num_steps=200, seed=seed)
        warmup = 10
        y_true = series[warmup:]
        naive_preds = naive_persistence(series)[warmup:]
        ma3_preds = moving_average_3(series)[warmup:]
        ewma_preds = exponential_weighted_moving_average(series, alpha=0.4)[warmup:]
        
        # Take up to 20 examples per seed to get 100 total examples across 5 seeds (> 50)
        for idx in range(min(20, len(y_true))):
            synthetic_examples.append({
                "input": f"Synthetic time series forecast step {warmup + idx} for seed {seed}",
                "output": str(float(y_true[idx])),
                "predict_naive": str(float(naive_preds[idx])),
                "predict_moving_average_3": str(float(ma3_preds[idx])),
                "predict_ewma": str(float(ewma_preds[idx])),
                "metadata_seed": str(seed),
                "metadata_step": str(warmup + idx)
            })
            
        del series, y_true, naive_preds, ma3_preds, ewma_preds
        gc.collect()

    dependency_datasets = []
    dep_path = "/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json"
    if os.path.exists(dep_path):
        with open(dep_path, "r") as f:
            dep_data = json.load(f)
            if isinstance(dep_data, dict) and "datasets" in dep_data:
                dependency_datasets = dep_data["datasets"]

    datasets_output = [
        {
            "dataset": "synthetic_autoinducer_buffer_time_series",
            "examples": synthetic_examples
        }
    ] + dependency_datasets

    method_out_data = {
        "metadata": {
            "title": "Moving Average vs Naive Persistence Forecasting",
            "description": "Comparison of 3-point moving average, EWMA, and naive persistence on synthetic time series."
        },
        "datasets": datasets_output
    }

    with open("method_out.json", "w") as f:
        json.dump(method_out_data, f, indent=2)

    print(f"Generated method_out.json with {len(synthetic_examples)} synthetic examples across datasets.")

if __name__ == "__main__":
    run_experiment()
