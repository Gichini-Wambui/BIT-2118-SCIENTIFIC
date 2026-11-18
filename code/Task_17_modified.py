"""Task 17: Euler method.
PART 1 - parameter change: step size h and cooling constant k.
PART 2 - new case: logistic population growth dP/dt = rP(1 - P/K), Euler vs exact."""
import numpy as np
import matplotlib.pyplot as plt

def euler_cool(h, k=0.12, T0=90., Ta=25., end=30.):
    t = np.arange(0, end + h / 2, h); T = np.zeros_like(t); T[0] = T0
    for i in range(len(t) - 1):
        T[i + 1] = T[i] + h * (-k * (T[i] - Ta))
    return t, T, Ta + (T0 - Ta) * np.exp(-k * t)

print("=== PART 1: Parameter changes ===")
for h in (5.0, 2.0, 1.0, 0.5, 0.1):
    t, T, ex = euler_cool(h)
    print(f"h={h:4.1f} min: Euler T(30)={T[-1]:6.2f} C  exact={ex[-1]:.2f} C  error={abs(T[-1]-ex[-1]):.4f}")
t, T, ex = euler_cool(1.0, k=0.30)
print(f"k=0.30 (faster cooling): Euler T(30)={T[-1]:.2f} C, exact {ex[-1]:.2f} C")
t, T, ex = euler_cool(10.0, k=0.30)
print(f"h=10 with k=0.30 (h*k=3 > 2): Euler values {np.round(T, 1)} -> unstable oscillation")

print("\n=== PART 2: Logistic population growth of a fish pond (tilapia) ===")
r, K, P0, h, end = 0.4, 5000.0, 200.0, 1.0, 30.0      # per month, fish, fish, month, months
t = np.arange(0, end + h / 2, h); P = np.zeros_like(t); P[0] = P0
for i in range(len(t) - 1):
    P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
exact = K / (1 + (K - P0) / P0 * np.exp(-r * t))
print(f"Euler population after {end:.0f} months: {P[-1]:.1f}")
print(f"Exact population after {end:.0f} months: {exact[-1]:.1f}")
print(f"Maximum absolute error over the run: {np.max(abs(P - exact)):.1f} fish")
print(f"Month when Euler population first exceeds K/2: {t[np.argmax(P > K/2)]:.0f} (exact: {np.log((K-P0)/P0)/r:.1f})")
plt.plot(t, P, "o-", label="Euler (h = 1 month)"); plt.plot(t, exact, label="Exact logistic")
plt.axhline(K, ls="--", lw=0.8); plt.xlabel("Months"); plt.ylabel("Fish in pond")
plt.title("Logistic growth in a fish pond"); plt.legend(); plt.grid(True)
plt.savefig("../figures/task17_modified.png", dpi=120, bbox_inches="tight"); plt.show()
