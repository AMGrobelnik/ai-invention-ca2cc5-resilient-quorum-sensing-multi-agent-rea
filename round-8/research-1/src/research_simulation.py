import numpy as np
import json

def run_wan_forecasting_simulation():
    np.random.seed(1337)
    n_steps = 100
    t = np.arange(n_steps)
    
    # Synthetic WAN propagation delay with diurnal/sinusoidal baseline, Gaussian jitter, and burst congestion spikes
    base = 50.0 + 15.0 * np.sin(t / 8.0)
    jitter = np.random.normal(0, 6.0, size=n_steps)
    spikes = np.zeros(n_steps)
    spike_indices = [15, 34, 52, 78, 91]
    for idx in spike_indices:
        spikes[idx] = 40.0 + np.random.uniform(0, 20.0)
        
    signal = base + jitter + spikes
    
    # Forecasting models starting at index 3
    # 1. Naive Last-Value: y_hat[t] = y[t-1]
    # 2. 3-Point Moving Average: y_hat[t] = mean(y[t-1], y[t-2], y[t-3])
    # 3. Adaptive EWMA (alpha = 0.35)
    
    y_true = signal[3:]
    y_naive = signal[2:-1]
    
    y_ma3 = np.array([np.mean(signal[i-3:i]) for i in range(3, n_steps)])
    
    y_ewma = []
    ewma_val = signal[2]
    alpha = 0.35
    for i in range(3, n_steps):
        ewma_val = alpha * signal[i-1] + (1 - alpha) * ewma_val
        y_ewma.append(ewma_val)
    y_ewma = np.array(y_ewma)
    
    # Metrics computation
    mse_naive = float(np.mean((y_true - y_naive)**2))
    mse_ma3 = float(np.mean((y_true - y_ma3)**2))
    mse_ewma = float(np.mean((y_true - y_ewma)**2))
    
    mae_naive = float(np.mean(np.abs(y_true - y_naive)))
    mae_ma3 = float(np.mean(np.abs(y_true - y_ma3)))
    mae_ewma = float(np.mean(np.abs(y_true - y_ewma)))
    
    improvement_mse = ((mse_naive - mse_ma3) / mse_naive) * 100.0
    improvement_mae = ((mae_naive - mae_ma3) / mae_naive) * 100.0
    
    results = {
        "n_steps": n_steps,
        "spike_count": len(spike_indices),
        "mse": {
            "naive_last_value": round(mse_naive, 4),
            "moving_average_3pt": round(mse_ma3, 4),
            "ewma_alpha_035": round(mse_ewma, 4)
        },
        "mae": {
            "naive_last_value": round(mae_naive, 4),
            "moving_average_3pt": round(mae_ma3, 4),
            "ewma_alpha_035": round(mae_ewma, 4)
        },
        "improvements_percent": {
            "mse_reduction_3pt_vs_naive": round(improvement_mse, 2),
            "mae_reduction_3pt_vs_naive": round(improvement_mae, 2)
        },
        "conclusion": f"3-point moving average outperforms naive last-value prediction by {improvement_mse:.2f}% MSE reduction on WAN telemetry simulation under stochastic jitter and congestion spikes."
    }
    
    with open('/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_8/gen_art/gen_art_research_1/simulation_results.json', 'w') as f:
        json.dump(results, f, indent=2)
        
    print("Simulation results saved successfully:", results)
    return results

if __name__ == '__main__':
    run_wan_forecasting_simulation()
