import numpy as np
import json

def run_simulation():
    np.random.seed(42)
    # Generate synthetic WAN latency time series with occasional spikes and jitter
    t = np.arange(50)
    # Base latency + sinusoidal fluctuation + random normal jitter + occasional burst spike
    base = 45.0 + 12.0 * np.sin(t / 4.0)
    jitter = np.random.normal(0, 4.5, size=50)
    spikes = np.zeros(50)
    spikes[[12, 28, 41]] = 35.0  # WAN transient congestion spikes
    signal = base + jitter + spikes

    # Forecasting comparison:
    # 1. Naive Last-Value Forecast (y_hat_t = y_{t-1})
    # 2. 3-Point Moving Average (y_hat_t = mean(y_{t-1}, y_{t-2}, y_{t-3}))
    # 3. Adaptive TTL / EWMA (alpha = 0.4)

    y_true = signal[3:]
    y_naive = signal[2:-1]

    y_ma3 = []
    for i in range(3, len(signal)):
        y_ma3.append(np.mean(signal[i-3:i]))
    y_ma3 = np.array(y_ma3)

    y_ewma = []
    alpha = 0.4
    curr_ewma = signal[2]
    for i in range(3, len(signal)):
        curr_ewma = alpha * signal[i-1] + (1 - alpha) * curr_ewma
        y_ewma.append(curr_ewma)
    y_ewma = np.array(y_ewma)

    mse_naive = float(np.mean((y_true - y_naive) ** 2))
    mae_naive = float(np.mean(np.abs(y_true - y_naive)))

    mse_ma3 = float(np.mean((y_true - y_ma3) ** 2))
    mae_ma3 = float(np.mean(np.abs(y_true - y_ma3)))

    mse_ewma = float(np.mean((y_true - y_ewma) ** 2))
    mae_ewma = float(np.mean(np.abs(y_true - y_ewma)))

    print(f"MSE Naive: {mse_naive:.4f}, MAE Naive: {mae_naive:.4f}")
    print(f"MSE MA(3): {mse_ma3:.4f}, MAE MA(3): {mae_ma3:.4f}")
    print(f"MSE EWMA:  {mse_ewma:.4f}, MAE EWMA:  {mae_ewma:.4f}")
    print(f"3-Point Moving Average beats Naive? {mse_ma3 < mse_naive}")

    results = {
        "series_length": int(len(signal)),
        "mse_naive": mse_naive,
        "mae_naive": mae_naive,
        "mse_ma3": mse_ma3,
        "mae_ma3": mae_ma3,
        "mse_ewma": mse_ewma,
        "mae_ewma": mae_ewma,
        "beats_naive": bool(mse_ma3 < mse_naive),
        "improvement_pct_mse": float((mse_naive - mse_ma3) / mse_naive * 100.0)
    }

    with open("simulation_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_simulation()
