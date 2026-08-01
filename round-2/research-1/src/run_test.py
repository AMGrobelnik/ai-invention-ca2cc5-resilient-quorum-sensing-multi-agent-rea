import numpy as np
import json
import os

def run_forecasting_test():
    np.random.seed(42)
    # Generate synthetic oscillatory series with noise
    t = np.linspace(0, 4 * np.pi, 50)
    series = np.sin(t) + 0.1 * np.random.randn(50)
    
    # Naive last-value forecast (t_i = series[i-1])
    # 3-point moving average forecast (t_i = mean(series[i-3:i]))
    
    y_true = series[3:]
    y_naive = series[2:-1]
    
    y_ma = []
    for i in range(3, len(series)):
        y_ma.append(np.mean(series[i-3:i]))
    y_ma = np.array(y_ma)
    
    mse_naive = np.mean((y_true - y_naive) ** 2)
    mse_ma = np.mean((y_true - y_ma) ** 2)
    
    results = {
        "series_length": len(series),
        "mse_naive": float(mse_naive),
        "mse_3point_ma": float(mse_ma),
        "naive_beats_ma": bool(mse_naive < mse_ma)
    }
    
    os.makedirs("/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_2/gen_art/gen_art_research_1", exist_ok=True)
    with open("/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_2/gen_art/gen_art_research_1/forecasting_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
        
    print("Forecasting test completed:", results)

if __name__ == "__main__":
    run_forecasting_test()
