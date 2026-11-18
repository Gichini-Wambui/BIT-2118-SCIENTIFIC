"""Task 20: Monte Carlo.
PART 1 - parameter change: capacity, standard deviation, number of simulations and random seed.
PART 2 - new case: probability that a 3-stage building project finishes within 60 days."""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

print("=== PART 1: Parameter changes (server overload) ===")
def overload(cap=1000., mean=850., std=120., N=100_000, seed=42):
    d = np.random.default_rng(seed).normal(mean, std, N)
    return (d > cap).mean()
print(f"original                     : {overload():.4%}   (exact normal tail {norm.sf(1000, 850, 120):.4%})")
print(f"capacity 1100                : {overload(cap=1100):.4%}   (exact {norm.sf(1100, 850, 120):.4%})")
print(f"std 200 (more uncertainty)   : {overload(std=200):.4%}   (exact {norm.sf(1000, 850, 200):.4%})")
print("N = 1,000 with 5 different seeds:", [f"{overload(N=1000, seed=s):.2%}" for s in range(5)])
print("N = 1,000,000, seeds 0-4      :", [f"{overload(N=1_000_000, seed=s):.3%}" for s in range(5)])

print("\n=== PART 2: Project finishing time (days) ===")
rng = np.random.default_rng(2024)
N = 200_000
foundation = rng.triangular(15, 20, 35, N)        # min, most likely, max
walls      = rng.triangular(20, 25, 45, N)
roof       = rng.triangular(8, 12, 20, N)
total = foundation + walls + roof                 # stages done one after another
deadline = 60
p_on_time = (total <= deadline).mean()
print(f"Mean total duration: {total.mean():.1f} days, standard deviation {total.std():.1f}")
print(f"Probability of finishing within {deadline} days: {p_on_time:.2%}")
print(f"90th percentile duration: {np.percentile(total, 90):.1f} days (90% of simulated projects finish by then)")
print(f"Planned 'most likely' duration (20+25+12): {20+25+12} days")
plt.hist(total, bins=80, density=True, alpha=0.8); plt.axvline(deadline, color="r", ls="--", label="Deadline (60 days)")
plt.xlabel("Total project duration (days)"); plt.ylabel("Density"); plt.title("Monte Carlo project duration"); plt.legend()
plt.savefig("../figures/task20_modified.png", dpi=120, bbox_inches="tight"); plt.show()
