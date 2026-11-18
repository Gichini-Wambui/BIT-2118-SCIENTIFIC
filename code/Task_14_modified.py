"""Task 14: curve fitting.
PART 1 - parameter change: change the model (linear, quadratic, cubic) and compare RMSE and extrapolation.
PART 2 - new case: logistic growth of a tree-seedling height (synthetic noisy data, seed 7)."""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

print("=== PART 1: Different models for the server data ===")
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
for deg in (1, 2, 3):
    c = np.polyfit(users, resp, deg)
    rmse = np.sqrt(np.mean((resp - np.polyval(c, users)) ** 2))
    print(f"degree {deg}: RMSE={rmse:6.2f} ms   prediction at 400 users={np.polyval(c, 400):7.2f} ms")
exp_model = lambda x, a, b, c: a * np.exp(b * x) + c
p, _ = curve_fit(exp_model, users, resp, p0=[10, 0.01, 70], maxfev=20000)
print(f"exponential a*exp(bx)+c: RMSE={np.sqrt(np.mean((resp - exp_model(users, *p))**2)):.2f} ms, prediction at 400 users={exp_model(400, *p):.2f} ms")

print("\n=== PART 2: Logistic growth of seedling height ===")
rng = np.random.default_rng(7)
weeks = np.arange(0, 21, 2, dtype=float)
true = lambda t, K, r, t0: K / (1 + np.exp(-r * (t - t0)))
height = true(weeks, 120, 0.45, 9) + rng.normal(0, 3, weeks.size)       # cm
popt, pcov = curve_fit(true, weeks, height, p0=[100, 0.3, 8])
perr = np.sqrt(np.diag(pcov))
K, r, t0 = popt
print(f"Fitted: K={K:.1f} cm (+/-{perr[0]:.1f}), r={r:.3f}/week (+/-{perr[1]:.3f}), t0={t0:.2f} weeks (+/-{perr[2]:.2f})")
print(f"RMSE: {np.sqrt(np.mean((height - true(weeks, *popt))**2)):.2f} cm")
print(f"Height predicted at week 30: {true(30, *popt):.1f} cm   | weeks to reach 90% of K: {t0 + np.log(9)/r:.1f}")
tt = np.linspace(0, 30, 200)
plt.scatter(weeks, height, label="Measured"); plt.plot(tt, true(tt, *popt), label="Logistic fit")
plt.axhline(K, ls="--", lw=0.8, label="Carrying capacity K")
plt.xlabel("Weeks"); plt.ylabel("Height (cm)"); plt.title("Seedling growth curve"); plt.legend(); plt.grid(True)
plt.savefig("../figures/task14_modified.png", dpi=120, bbox_inches="tight"); plt.show()
