"""Task 10 (modified): bisection and fixed-point.
PART 1 - parameter change: fixed-point start value, and a stronger coefficient (10 -> 500) that breaks convergence.
PART 2 - new case: break-even quantities of a product whose price falls as volume rises."""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

print("=== PART 1: Parameter changes ===")
def fixed_point(g, T0, tol=1e-10, n=100):
    T = T0
    for k in range(1, n + 1):
        Tn = g(T)
        if abs(Tn - T) < tol: return Tn, k
        T = Tn
    return T, n
g = lambda T: 25 + 10 * np.exp(-T / 20)
for T0 in (30.0, 20.0, 100.0):
    r, k = fixed_point(g, T0)
    print(f"start T0={T0:5.1f}: root={r:.6f} in {k} iterations")
g2 = lambda T: 25 + 500 * np.exp(-T / 20)
exact2 = root_scalar(lambda T: T - 25 - 500*np.exp(-T/20), bracket=[20, 100], method='bisect').root
print(f"coefficient 500: exact root (bisection) = {exact2:.4f}; |g'(root)| = {abs(-25*np.exp(-exact2/20)):.2f} > 1")
T = 50.0
print("fixed-point iterates:", end=" ")
for k in range(8):
    T = g2(T); print(f"{T:.2f}", end=" ")
print("\n-> the iterates oscillate away from the root (fixed-point fails); bisection still works")
for tol in (1e-2, 1e-6, 1e-10):
    s = root_scalar(lambda T: T - 25 - 10*np.exp(-T/20), bracket=[20, 40], method="bisect", xtol=tol)
    print(f"bisection xtol={tol:g}: iterations={s.iterations}")

print("\n=== PART 2: Break-even analysis ===")
# revenue = q * 120 * exp(-q/2000)  (price falls as volume rises); cost = 5000 + 30 q
def profit(q): return 120 * q * np.exp(-q / 2000) - 5000 - 30 * q
low = root_scalar(profit, bracket=[10, 500], method="bisect", xtol=1e-6)
high = root_scalar(profit, bracket=[2000, 6000], method="bisect", xtol=1e-6)
print(f"Lower break-even quantity: {low.root:.2f} units ({low.iterations} iterations)")
print(f"Upper break-even quantity: {high.root:.2f} units ({high.iterations} iterations)")
q = np.linspace(0, 6000, 600)
best = q[np.argmax(profit(q))]
print(f"Profitable between {low.root:.0f} and {high.root:.0f} units; max profit ~{profit(best):,.0f} near q={best:.0f}")
plt.plot(q, profit(q)); plt.axhline(0, color="k", lw=0.8)
plt.axvline(low.root, ls="--"); plt.axvline(high.root, ls="--")
plt.xlabel("Quantity sold"); plt.ylabel("Profit"); plt.title("Break-even points"); plt.grid(True)
plt.savefig("../figures/task10_modified.png", dpi=120, bbox_inches="tight"); plt.show()
