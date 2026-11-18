"""Task 3 (modified): vectorization.
PART 1 - parameter change: array size N = 100, 10_000, 1_000_000.
PART 2 - new case: mobile-money fee of 1.5% (min 10, max 100 KES) on 1,000,000 transactions."""
import numpy as np, timeit

rng = np.random.default_rng(42)

print("=== PART 1: Effect of array size (original latency problem) ===")
for N in (100, 10_000, 1_000_000):
    lat = rng.uniform(5, 250, N)
    def loop():
        out = []
        for v in lat:
            out.append((v / 1000.0) ** 2)
        return out
    def vec():
        return (lat / 1000.0) ** 2
    reps = max(1, 1_000_000 // N)
    t_loop = timeit.timeit(loop, number=reps) / reps
    t_vec = timeit.timeit(vec, number=reps) / reps
    print(f"N={N:>9,}: loop={t_loop:.6f}s vectorized={t_vec:.6f}s speed-up={t_loop/t_vec:.1f}x")

print("\n=== PART 2: Transaction fees ===")
amounts = rng.uniform(50, 20_000, 1_000_000)      # KES, simulated

def fee_loop():
    fees = []
    for a in amounts:
        f = 0.015 * a
        if f < 10: f = 10
        elif f > 100: f = 100
        fees.append(f)
    return fees

def fee_vec():
    return np.clip(0.015 * amounts, 10, 100)       # clip applies min and max at once

t_loop = timeit.timeit(fee_loop, number=1)
t_vec = timeit.timeit(fee_vec, number=3) / 3
fees = fee_vec()
print("First five amounts:", np.round(amounts[:5], 2))
print("First five fees   :", np.round(fees[:5], 2))
print(f"Total fees collected: KES {fees.sum():,.0f}")
print(f"Share of transactions at the KES 100 cap: {(fees == 100).mean():.1%}")
print(f"Loop: {t_loop:.4f}s | Vectorized: {t_vec:.4f}s | speed-up {t_loop/t_vec:.1f}x")
print("Results identical:", np.allclose(fees, fee_loop()))
