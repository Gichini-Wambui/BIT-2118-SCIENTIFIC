"""Task 13: interpolation.
PART 1 - parameter change: different query time, and one hourly value changed (noisy sensor).
PART 2 - new case: fill missing river-level readings (hours 3 and 4 lost) and validate against the true values."""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

print("=== PART 1: Parameter changes ===")
hours = np.arange(8, 15, dtype=float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
for label, y in (("original", temp), ("outlier at 11:00 (24.0 -> 30.0)", np.where(hours == 11, 30.0, temp))):
    lin, cub = interp1d(hours, y), CubicSpline(hours, y)
    for t in (10.5, 13.5):
        print(f"{label:32s} t={t}: linear={float(lin(t)):.2f}  cubic={float(cub(t)):.2f}")
cub = CubicSpline(hours, temp)
print("Extrapolation test, cubic at 16:00 =", round(float(cub(16.0)), 2), "(unreliable outside data range)")

print("\n=== PART 2: River level with two missing readings ===")
t_all = np.arange(0, 9, dtype=float)                       # hours 0..8
level_true = np.array([1.20, 1.25, 1.40, 1.70, 2.10, 2.35, 2.40, 2.30, 2.15])   # metres (synthetic data)
known = np.array([0, 1, 2, 5, 6, 7, 8])                    # hours 3 and 4 are missing
lin = interp1d(t_all[known], level_true[known])
cub = CubicSpline(t_all[known], level_true[known])
for h in (3, 4):
    print(f"hour {h}: true={level_true[h]:.2f} m  linear={float(lin(h)):.2f} m (err {abs(lin(h)-level_true[h]):.2f})"
          f"  cubic={float(cub(h)):.2f} m (err {abs(cub(h)-level_true[h]):.2f})")
tt = np.linspace(0, 8, 200)
plt.plot(t_all, level_true, "k:", label="True (hidden) values")
plt.scatter(t_all[known], level_true[known], zorder=3, label="Recorded")
plt.plot(tt, lin(tt), label="Linear"); plt.plot(tt, cub(tt), label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("River level (m)"); plt.title("Filling missing river-level data")
plt.legend(); plt.grid(True)
plt.savefig("../figures/task13_modified.png", dpi=120, bbox_inches="tight"); plt.show()
