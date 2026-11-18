# Task 6: Solution of Systems of Linear Equations

*Programs:* `code/Task_06_linear_systems.py` (original) and `code/Task_06_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
A = [[4,2],[8,12]] (CPU and memory per server type) and b = [20, 72] (observed totals). Operation: solve Ax = b with `np.linalg.solve`; verify using the residual b − Ax.

## 2. Original output and its meaning
```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```
3 Type A and 4 Type B servers are active: 4·3+2·4 = 20 CPU and 8·3+12·4 = 72 GB. The residual is zero, so the solution reproduces the observations exactly.

## 3. Parameter change and how the result changes
Changing the totals to [24, 80] gives 4 A and 4 B. Totals [20, 30] give A = 5.625 and B = −1.25: a negative server count is impossible, so the data are inconsistent with the model. Making the second equation a multiple of the first gives a singular matrix (determinant 0) and `solve` raises `LinAlgError`: there is no unique solution.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** Balance the combustion of propane: a C₃H₈ + b O₂ → c CO₂ + d H₂O. Atom counts give linear equations; fix a = 1 to remove the scaling freedom. C: c = 3; H: 2d = 8; O: 2b = 2c + d.

**Output of `Task_06_modified.py`:**
```text
=== PART 1: Parameter changes ===
Totals CPU/mem=[20.0, 72.0] -> Type A=3.000, Type B=4.000
Totals CPU/mem=[24.0, 80.0] -> Type A=4.000, Type B=4.000
Totals CPU/mem=[20.0, 30.0] -> Type A=5.625, Type B=-1.250
(last case gives a negative server count: the observed totals are inconsistent with the model)
Determinant of dependent system: 0.0
np.linalg.solve failed: Singular matrix

=== PART 2: Balancing  a C3H8 + b O2 -> c CO2 + d H2O  (set a = 1) ===
b=5, c=3, d=4
Balanced: C3H8 + 5 O2 -> 3 CO2 + 4 H2O
Residual: [0. 0. 0.]
```
**Interpretation:** The solver gives b = 5, c = 3, d = 4: **C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O**. The residual is zero, so atoms are conserved. Chemical balancing is a linear system because each element gives one linear equation.

