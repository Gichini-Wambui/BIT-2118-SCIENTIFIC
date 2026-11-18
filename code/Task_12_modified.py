"""Task 12: nonlinear equations.
PART 1 - parameter change: circle radius 2 -> 3, and a radius (0.5) where there is no intersection.
PART 2 - new case: a ball thrown at a hillside - where does it land? (polynomial roots + nonlinear solve)"""
import numpy as np
from scipy.optimize import root

print("=== PART 1: Parameter changes ===")
def system(r):
    def eq(z):
        x, y = z
        return [x**2 + y**2 - r**2, y - (x**2 - 1)]
    return eq
for r in (2.0, 3.0, 0.5):
    print(f"radius {r}:")
    for g in ([1.0, 1.0], [-1.0, 1.0]):
        s = root(system(r), g)
        print(f"   guess {g} -> ({s.x[0]:.4f}, {s.x[1]:.4f})  converged={s.success}  residual norm={np.linalg.norm(system(r)(s.x)):.1e}")

print("\n=== PART 2: Ball thrown at a hillside ===")
v, angle, g = 25.0, np.deg2rad(50), 9.81
a = -g / (2 * v**2 * np.cos(angle)**2)       # trajectory y = a x^2 + tan(angle) x
b = np.tan(angle)
slope, start = 0.25, 0.0                      # hill: y = 0.25 x, rising from the launch point
# trajectory = hill  ->  a x^2 + (b - slope) x = 0
coeffs = [a, b - slope, -start]
roots = np.roots(coeffs)
print("Polynomial roots of the intersection equation:", np.round(roots, 3))
x_land = max(roots.real)
print(f"Ball lands at x = {x_land:.2f} m, height y = {slope * x_land:.2f} m on the hill")
def eqs(z):
    x, y = z
    return [y - (a * x**2 + b * x), y - slope * x]
s = root(eqs, [45.0, 11.0])
print(f"scipy.optimize.root check (guess 45, 11): x={s.x[0]:.2f}, y={s.x[1]:.2f}, converged={s.success}")
s0 = root(eqs, [2.0, 0.5])
print(f"Different guess (2, 0.5) finds the other root: x={s0.x[0]:.2f}, y={s0.x[1]:.2f} (the launch point itself)")
x = np.linspace(0, x_land, 5)
print("Flight path x (m):", np.round(x, 1), "-> y (m):", np.round(a * x**2 + b * x, 2))
