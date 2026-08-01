import numpy as np
import json

def run_simulation():
    np.random.seed(42)
    # Generate synthetic time series (e.g., agent response latency / quorum TTL buffer values with jitter)
    steps = 50
    true_vals = 100 + np.cumsum(np.random.normal(0, 5, size=steps))
    # Add observation noise
    noise = np.random.normal(0, 3, size=steps)
    obs = true_vals + noise

    naive_preds = []
    ma3_preds = []
    actuals = []

    for t in range(3, steps):
        # Naive forecast: last observed value
        naive_pred = obs[t-1]
        # 3-point moving average forecast
        ma3_pred = np.mean(obs[t-3:t])
        
        naive_preds.append(naive_pred)
        ma3_preds.append(ma3_pred)
        actuals.append(obs[t])

    naive_mse = np.mean((np.array(actuals) - np.array(naive_preds)) ** 2)
    ma3_mse = np.mean((np.array(actuals) - np.array(ma3_preds)) ** 2)

    results = {
        "steps": steps,
        "naive_mse": float(naive_mse),
        "ma3_mse": float(ma3_mse),
        "improvement_pct": float((naive_mse - ma3_mse) / naive_mse * 100)
    }

    with open("/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_7/gen_art/gen_art_research_1/simulation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Simulation results:", results)

if __name__ == "__main__":
    run_simulation()
