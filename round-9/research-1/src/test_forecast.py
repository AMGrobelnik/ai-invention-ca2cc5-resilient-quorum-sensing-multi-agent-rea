import numpy as np
import json

def test_forecasting():
    np.random.seed(123)
    t = np.linspace(0, 4 * np.pi, 50)
    series_noisy = np.sin(t) * 10 + 50 + np.random.normal(0, 3.5, 50)

    y_true = series_noisy[3:]
    y_naive = series_noisy[2:-1]

    y_ma = []
    for i in range(3, len(series_noisy)):
        y_ma.append(np.mean(series_noisy[i-3:i]))
    y_ma = np.array(y_ma)

    mse_naive = np.mean((y_true - y_naive) ** 2)
    mse_ma = np.mean((y_true - y_ma) ** 2)

    improvement = (mse_naive - mse_ma) / mse_naive * 100

    results = {
        "series_length": len(series_noisy),
        "mse_naive": float(mse_naive),
        "mse_3point_ma": float(mse_ma),
        "improvement_pct": float(improvement),
        "ma_beats_naive": bool(mse_ma < mse_naive)
    }

    with open("forecasting_test_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Forecasting test results:", results)

if __name__ == "__main__":
    test_forecasting()
