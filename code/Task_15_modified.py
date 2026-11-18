"""Task 15: numerical differentiation.
PART 1 - parameter change: step size h on a known function, forward vs central difference.
PART 2 - new case: acceleration of a matatu from non-uniformly sampled speed data (np.gradient)."""
import numpy as np
import matplotlib.pyplot as plt

print("=== PART 1: Effect of h on d/dx sin(x) at x = 1 (exact = cos(1)) ===")
exact = np.cos(1.0)
print(f"{'h':>8} {'forward err':>13} {'central err':>13}")
for h in (1.0, 0.1, 0.01, 0.001, 1e-6, 1e-10, 1e-14):
    fwd = (np.sin(1 + h) - np.sin(1)) / h
    cen = (np.sin(1 + h) - np.sin(1 - h)) / (2 * h)
    print(f"{h:8.0e} {abs(fwd - exact):13.3e} {abs(cen - exact):13.3e}")

print("\n=== PART 2: Matatu acceleration ===")
t = np.array([0, 2, 4, 5, 8, 10, 14, 16, 20], dtype=float)                # s (uneven sampling)
v_kmh = np.array([0, 18, 32, 38, 52, 58, 50, 48, 48], dtype=float)         # km/h
v = v_kmh / 3.6                                                            # m/s
a = np.gradient(v, t)                                                      # handles uneven spacing
for ti, vi, ai in zip(t, v, a):
    print(f"t={ti:4.0f}s  speed={vi:5.2f} m/s  acceleration={ai:6.2f} m/s^2")
print(f"Maximum acceleration: {a.max():.2f} m/s^2 at t={t[a.argmax()]:.0f}s")
print(f"Maximum braking: {a.min():.2f} m/s^2 at t={t[a.argmin()]:.0f}s")
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(6, 5))
ax[0].plot(t, v, "o-"); ax[0].set_ylabel("Speed (m/s)"); ax[0].grid(True)
ax[1].plot(t, a, "o-", color="tab:red"); ax[1].axhline(0, lw=0.8, color="k")
ax[1].set(xlabel="Time (s)", ylabel="Acceleration (m/s^2)"); ax[1].grid(True)
plt.savefig("../figures/task15_modified.png", dpi=120, bbox_inches="tight"); plt.show()
