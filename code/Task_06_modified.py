"""Task 6 (modified): linear systems.
PART 1 - parameter change: new observed totals; then a singular (dependent) system.
PART 2 - new case: balancing the combustion of propane  a C3H8 + b O2 -> c CO2 + d H2O."""
import numpy as np

A = np.array([[4., 2.], [8., 12.]])

print("=== PART 1: Parameter changes ===")
for b in ([20., 72.], [24., 80.], [20., 30.]):
    x = np.linalg.solve(A, b)
    print(f"Totals CPU/mem={b} -> Type A={x[0]:.3f}, Type B={x[1]:.3f}")
print("(last case gives a negative server count: the observed totals are inconsistent with the model)")
S = np.array([[4., 2.], [8., 4.]])        # second row is 2 x first row
print("Determinant of dependent system:", np.linalg.det(S))
try:
    np.linalg.solve(S, np.array([20., 40.]))
except np.linalg.LinAlgError as e:
    print("np.linalg.solve failed:", e)

print("\n=== PART 2: Balancing  a C3H8 + b O2 -> c CO2 + d H2O  (set a = 1) ===")
# Unknowns [b, c, d];   C: 3 = c    H: 8 = 2d    O: 2b = 2c + d
M = np.array([[0., 1., 0.],     # c = 3
              [0., 0., 2.],     # 2d = 8
              [2., -2., -1.]])  # 2b - 2c - d = 0
rhs = np.array([3., 8., 0.])
b_, c_, d_ = np.linalg.solve(M, rhs)
print(f"b={b_:.0f}, c={c_:.0f}, d={d_:.0f}")
print(f"Balanced: C3H8 + {b_:.0f} O2 -> {c_:.0f} CO2 + {d_:.0f} H2O")
print("Residual:", rhs - M @ np.array([b_, c_, d_]))
