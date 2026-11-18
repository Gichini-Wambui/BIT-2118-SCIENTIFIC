"""Task 8 (modified): iterative methods.
PART 1 - parameter change: tolerance 1e-8 -> 1e-3, and boundary temperature 100 -> 150 C.
PART 2 - new case: a metal rod with 9 interior nodes, ends held at 80 C and 30 C, plus a heat source in the middle."""
import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        xn = (b - R @ x) / D; e = np.linalg.norm(xn - x, np.inf); errs.append(e); x = xn
        if e < tol: break
    return x, errs

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        e = np.linalg.norm(x - old, np.inf); errs.append(e)
        if e < tol: break
    return x, errs

def tridiag(n):
    return 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)

print("=== PART 1: Parameter changes (5-node model) ===")
A = tridiag(5)
for tol in (1e-3, 1e-8):
    b = np.array([100., 0, 0, 0, 20.])
    _, ej = jacobi(A, b, tol); xg, eg = gauss_seidel(A, b, tol)
    print(f"tol={tol:g}: Jacobi {len(ej)} iterations, Gauss-Seidel {len(eg)} iterations")
b150 = np.array([150., 0, 0, 0, 20.])
print("Left boundary 150 C ->", np.round(np.linalg.solve(A, b150), 3))

print("\n=== PART 2: Rod with 9 interior nodes, ends 80 C and 30 C, heater at node 5 ===")
n = 9
A = tridiag(n)
b = np.zeros(n); b[0] = 80; b[-1] = 30; b[4] += 10      # +10 = heat source term at the middle node
x_j, ej = jacobi(A, b); x_g, eg = gauss_seidel(A, b); x_d = np.linalg.solve(A, b)
print("Direct solution      :", np.round(x_d, 3))
print("Jacobi solution      :", np.round(x_j, 3), f"({len(ej)} iterations)")
print("Gauss-Seidel solution:", np.round(x_g, 3), f"({len(eg)} iterations)")
print("Max difference iterative vs direct:", f"{max(abs(x_j-x_d).max(), abs(x_g-x_d).max()):.2e}")
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
pos = np.arange(0, n + 2)
ax[0].plot(pos, np.concatenate([[80], x_d, [30]]), "o-")
ax[0].set(xlabel="Node position", ylabel="Temperature (C)", title="Rod temperature profile"); ax[0].grid(True)
ax[1].semilogy(ej, label="Jacobi"); ax[1].semilogy(eg, label="Gauss-Seidel")
ax[1].set(xlabel="Iteration", ylabel="Maximum change", title="Convergence"); ax[1].legend(); ax[1].grid(True)
plt.savefig("../figures/task08_modified.png", dpi=120, bbox_inches="tight"); plt.show()
