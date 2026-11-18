"""Task 9 (modified): eigenvalues.
PART 1 - parameter change: add a link A-D to the network and see how importance shifts.
PART 2 - new case: PageRank for 4 web pages with damping factor 0.85 (power iteration vs eigenvector)."""
import numpy as np

nodes = ["A", "B", "C", "D"]
def centrality(adj):
    w, v = np.linalg.eig(adj)
    i = np.argmax(w.real)
    vec = np.abs(v[:, i].real)
    return w[i].real, vec / vec.sum()

print("=== PART 1: Parameter change (add edge A-D) ===")
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
for name, M in (("original", A), ("with A-D link", A2)):
    lam, c = centrality(M)
    print(f"{name:14s} lambda={lam:.4f}  importance=" + ", ".join(f"{n}:{s:.4f}" for n, s in zip(nodes, c)))

print("\n=== PART 2: PageRank (links: A->B,C ; B->C ; C->A ; D->C) ===")
links = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}
idx = {n: i for i, n in enumerate(nodes)}
M = np.zeros((4, 4))                       # column-stochastic: column j = where page j sends its rank
for src, outs in links.items():
    for dst in outs:
        M[idx[dst], idx[src]] = 1 / len(outs)
d = 0.85
G = d * M + (1 - d) / 4 * np.ones((4, 4))  # Google matrix
r = np.ones(4) / 4
for it in range(1, 200):
    r_new = G @ r
    if np.abs(r_new - r).sum() < 1e-12: break
    r = r_new
print(f"Power iteration converged in {it} steps")
w, v = np.linalg.eig(G)
pr = np.abs(v[:, np.argmax(w.real)].real); pr /= pr.sum()
print("Dominant eigenvalue of G:", round(w.real.max(), 6))
for n, a, b in zip(nodes, r_new, pr):
    print(f"Page {n}: power iteration={a:.4f}  eigenvector={b:.4f}")
print("Ranking:", " > ".join(sorted(nodes, key=lambda n: -r_new[idx[n]])))
