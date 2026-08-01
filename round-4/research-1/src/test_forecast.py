import numpy as np
import json

def test_forecasting():
    np.random.seed(42)
    # Generate synthetic time series (e.g., network latency with jitter)
    t = np.arange(30)
    signal = 50 + 10 * np.sin(t / 3.0) + np.random.normal(0, 3, size=30)
    
    # Naive last-value forecast (predict t from t-1)
    # MA(3) forecast (predict t from mean of t-1, t-2, t-3)
    
    y_true = signal[3:]
    y_naive = signal[2:-1]
    
    y_ma3 = []
    for i in range(3, len(signal)):
        y_ma3.append(np.mean(signal[i-3:i]))
    y_ma3 = np.array(y_ma3)
    
    mse_naive = np.mean((y_true - y_naive) ** 2)
    mse_ma3 = np.mean((y_true - y_ma3) ** 2)
    
    print(f"MSE Naive: {mse_naive:.4f}")
    print(f"MSE MA(3): {mse_ma3:.4f}")
    
    results = {
        "mse_naive": float(mse_naive),
        "mse_ma3": float(mse_ma3),
        "beats_naive": bool(mse_ma3 < mse_naive)
    }
    
    with open("simulation_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    test_forecasting()
