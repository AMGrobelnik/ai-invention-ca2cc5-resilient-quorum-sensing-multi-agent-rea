import json
import numpy as np

def run_simulation():
    np.random.seed(42)
    # Generate synthetic time series with trend and jitter (simulating WAN RTT / buffer metrics)
    n = 50
    t = np.arange(n)
    trend = 100 + 0.5 * t
    noise = np.random.normal(0, 10, size=n)
    series = trend + noise

    # Naive forecast: y_hat[t] = y[t-1]
    # MA(3) forecast: y_hat[t] = mean(y[t-3:t])
    
    y_true = []
    y_naive = []
    y_ma3 = []
    
    for i in range(3, n):
        y_true.append(series[i])
        y_naive.append(series[i-1])
        y_ma3.append(np.mean(series[i-3:i]))
        
    y_true = np.array(y_true)
    y_naive = np.array(y_naive)
    y_ma3 = np.array(y_ma3)
    
    mse_naive = np.mean((y_true - y_naive) ** 2)
    mse_ma3 = np.mean((y_true - y_ma3) ** 2)
    
    improvement = (mse_naive - mse_ma3) / mse_naive * 100
    
    results = {
        "series_length": n,
        "mse_naive": float(mse_naive),
        "mse_ma3": float(mse_ma3),
        "beats_naive": bool(mse_ma3 < mse_naive),
        "improvement_pct_mse": float(improvement)
    }
    
    print(json.dumps(results, indent=2))
    with open("simulation_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_simulation()
