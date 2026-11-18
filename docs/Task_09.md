# Task 9: Eigenvalues and Eigenvectors

*Programs:* `code/Task_09_eigenvalues.py` (original) and `code/Task_09_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Adjacency matrix of a 4-node undirected network (A–B, A–C, B–C, B–D, C–D). Operation: `np.linalg.eig`, pick the largest eigenvalue and its eigenvector, normalise it to sum to 1.

## 2. Original output and its meaning
```text
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```
Dominant eigenvalue ≈ 2.5616. Nodes B and C (each linked to three nodes) score 0.2808; A and D (two links each) score 0.2192. The verification error ~1e-15 confirms Av = λv. B and C are the most structurally influential.

## 3. Parameter change and how the result changes
Adding the link A–D turns the graph into a complete graph where every node has three links. The dominant eigenvalue becomes 3.0 and all four scores become 0.25: the extra edge removes the difference in importance.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** PageRank for four web pages with links A→B,C; B→C; C→A; D→C and damping factor 0.85. The Google matrix G = 0.85·M + 0.15/4 is column-stochastic, so its dominant eigenvalue is 1. Solved by power iteration and by `eig`.

**Output of `Task_09_modified.py`:**
```text
=== PART 1: Parameter change (add edge A-D) ===
original       lambda=2.5616  importance=A:0.2192, B:0.2808, C:0.2808, D:0.2192
with A-D link  lambda=3.0000  importance=A:0.2500, B:0.2500, C:0.2500, D:0.2500

=== PART 2: PageRank (links: A->B,C ; B->C ; C->A ; D->C) ===
Power iteration converged in 56 steps
Dominant eigenvalue of G: 1.0
Page A: power iteration=0.3725  eigenvector=0.3725
Page B: power iteration=0.1958  eigenvector=0.1958
Page C: power iteration=0.3941  eigenvector=0.3941
Page D: power iteration=0.0375  eigenvector=0.0375
Ranking: C > A > B > D
```
**Interpretation:** Ranking C > A > B > D (scores 0.394, 0.373, 0.196, 0.038). C is top because three pages link to it, A gets a big share from C, and D has no incoming links so it only receives the teleport share. Power iteration (56 steps) and the eigenvector agree to 4 decimals.

