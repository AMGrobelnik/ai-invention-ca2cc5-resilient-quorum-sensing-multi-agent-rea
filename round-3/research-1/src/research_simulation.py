import numpy as np
import json
import os

def simulate_delayed_quorum(N=16, steps=100, gamma=0.4, beta=0.8, k=2.5, theta=0.5, mean_delay=3, jitter_std=1.0):
    np.random.seed(42)
    max_delay = int(mean_delay + 3 * jitter_std) + 2
    history_length = max_delay + 5
    total_len = history_length + steps
    a = np.zeros((total_len, N))
    a[:history_length] = np.random.uniform(0.1, 0.3, size=(history_length, N))
    
    trajectory = []
    
    for t in range(history_length, total_len):
        delays = np.random.normal(mean_delay, jitter_std, size=(N, N))
        delays = np.clip(np.round(delays), 0, t - 1).astype(int)
        
        current_state = np.zeros(N)
        for i in range(N):
            sum_signals = 0.0
            for j in range(N):
                d_ij = delays[j, i]
                past_idx = t - 1 - d_ij
                past_val = a[past_idx, j]
                activation = 1.0 / (1.0 + np.exp(-k * (past_val - theta)))
                sum_signals += activation
                
            noise = np.random.normal(0, 0.02)
            next_a = (1.0 - gamma) * a[t - 1, i] + (beta / N) * sum_signals + noise
            current_state[i] = np.clip(next_a, 0.0, 1.0)
            
        a[t] = current_state
        trajectory.append(float(np.mean(current_state)))
        
    return trajectory

def run_forecasting_test(series):
    y = np.array(series)
    n = len(y)
    naive_errors = []
    ma_errors = []
    
    for t in range(3, n):
        true_val = y[t]
        naive_pred = y[t-1]
        ma_pred = np.mean(y[t-3:t])
        
        naive_errors.append((true_val - naive_pred) ** 2)
        ma_errors.append((true_val - ma_pred) ** 2)
        
    naive_mse = float(np.mean(naive_errors))
    ma_mse = float(np.mean(ma_errors))
    
    return {
        "naive_mse": naive_mse,
        "ma_3pt_mse": ma_mse,
        "ma_beats_naive": ma_mse < naive_mse
    }

if __name__ == "__main__":
    results = {}
    for jitter in [0.5, 1.0, 2.0]:
        traj = simulate_delayed_quorum(jitter_std=jitter)
        fc = run_forecasting_test(traj)
        results[f"jitter_{jitter}"] = {
            "final_mean_activation": traj[-1],
            "max_activation": max(traj),
            "forecasting": fc
        }
        
    with open("simulation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Simulation completed successfully and saved to simulation_results.json")
