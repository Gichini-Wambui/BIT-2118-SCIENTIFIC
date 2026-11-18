"""Task 7 (modified): LU decomposition.
PART 1 - parameter change: weaker diagonal in A, and a timing test on a 600x600 system with 300 right-hand sides.
PART 2 - new case: three-loop electrical circuit (mesh currents) with several supply-voltage scenarios."""
import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve

print("=== PART 1: Parameter changes ===")
A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
A2 = A.copy(); A2[2, 2] = 0.2668                  # det(A)=15*A33-4 -> almost zero: nearly singular
b = np.array([15., 10., 10.])
for name, M in (("original", A), ("nearly singular", A2)):
    print(f"{name:16s} cond={np.linalg.cond(M):10.2f}  solution={np.round(np.linalg.solve(M, b), 4)}")
rng = np.random.default_rng(1)
n, m = 600, 300
Big = rng.random((n, n)) + n * np.eye(n)
B = rng.random((n, m))
t_repeat = timeit.timeit(lambda: [np.linalg.solve(Big, B[:, j]) for j in range(m)], number=1)
def with_lu():
    lu, piv = lu_factor(Big)
    return [lu_solve((lu, piv), B[:, j]) for j in range(m)]
t_lu = timeit.timeit(with_lu, number=1)
print(f"300 right-hand sides: repeated solve {t_repeat:.3f}s | one LU + 300 lu_solve {t_lu:.3f}s")

print("\n=== PART 2: Mesh-current analysis of a 3-loop circuit ===")
# Resistances (ohm): loop1 R=10, loop2 R=20, loop3 R=15; shared R12=5, R23=8
R = np.array([[10 + 5, -5,       0],
              [-5,     20 + 5 + 8, -8],
              [0,      -8,       15 + 8]], dtype=float)
scenarios = {"Normal (12,0,6 V)": [12, 0, 6], "Battery 1 doubled (24,0,6 V)": [24, 0, 6], "Loop 2 source on (12,9,6 V)": [12, 9, 6]}
lu, piv = lu_factor(R)
for name, V in scenarios.items():
    I = lu_solve((lu, piv), np.array(V, dtype=float))
    print(f"{name:30s} currents (A) = {np.round(I, 4)}  residual={np.linalg.norm(V - R @ I):.1e}")
