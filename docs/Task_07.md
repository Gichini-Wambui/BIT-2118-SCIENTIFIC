# Task 7: Gaussian Elimination and LU Decomposition

*Programs:* `code/Task_07_gaussian_lu.py` (original) and `code/Task_07_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
A 3×3 coefficient matrix A and three measurement vectors b. Operations: factor A = PLU once (`lu_factor`), then solve each b by forward and back substitution (`lu_solve`).

## 2. Original output and its meaning
```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```
Set 1 gives x = [5, 5, 5], matching the direct `np.linalg.solve` result; sets 2 and 3 give other solutions from the same factorisation. Residual norms ~1e-15 are round-off level, so the solutions are accurate.

## 3. Parameter change and how the result changes
Reducing A₃₃ to 0.2668 makes det(A) = 15·A₃₃ − 4 almost zero; the condition number jumps from 2.4 to about 41,000 and the solution explodes to ≈[6838, 27337, 102500]: small changes in a nearly singular system produce huge changes in the answer. I also timed 300 right-hand sides on a 600×600 system: one LU factorisation plus 300 cheap solves was far faster than 300 full solves (timings are machine-dependent).

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** Mesh-current analysis of a three-loop circuit with resistances 10, 20, 15 Ω in the loops and 5 Ω and 8 Ω shared between neighbouring loops. Unknowns are the loop currents; the right-hand side is the loop source voltages. Resistor values and voltages are illustrative.

**Output of `Task_07_modified.py`:**
```text
=== PART 1: Parameter changes ===
original         cond=      2.39  solution=[5. 5. 5.]
nearly singular  cond=  41209.36  solution=[  6838.  27337. 102500.]
300 right-hand sides: repeated solve 1.721s | one LU + 300 lu_solve 0.066s

=== PART 2: Mesh-current analysis of a 3-loop circuit ===
Normal (12,0,6 V)              currents (A) = [0.8711 0.2132 0.335 ]  residual=9.9e-16
Battery 1 doubled (24,0,6 V)   currents (A) = [1.7178 0.3533 0.3838]  residual=3.8e-15
Loop 2 source on (12,9,6 V)    currents (A) = [0.9761 0.5284 0.4447]  residual=3.7e-15
```
**Interpretation:** R is factored once and reused for three voltage scenarios. Doubling battery 1 roughly doubles loop-1 current (0.87 → 1.72 A), and switching on a source in loop 2 raises all currents. Residuals ~1e-15 confirm accuracy. This 'same A, different b' situation is exactly where LU pays off.

