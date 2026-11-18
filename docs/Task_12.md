# Task 12: Polynomial and Nonlinear Equation Solving

*Programs:* `code/Task_12_nonlinear_equations.py` (original) and `code/Task_12_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Circle x² + y² = 4 and parabola y = x² − 1 as two residual equations. `scipy.optimize.root` is run from two starting guesses (1,1) and (−1,1).

## 2. Original output and its meaning
```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```
Intersections at (±1.5175, 1.3028). Residuals ~1e-13 mean both equations are satisfied. The two starts find the two mirror-image solutions, showing why several guesses are needed.

## 3. Parameter change and how the result changes
Radius 3 moves the intersections to (±1.8364, 2.3723). Radius 0.5 has no intersection: the solver returns `converged=False` with a large residual (0.35), so always check `success` and the residual.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** A ball launched at 25 m/s and 50° up a hill sloping upward at 0.25 (y = 0.25x). Trajectory: y = x·tan θ − g x²/(2v²cos²θ), g = 9.81 m/s². No air resistance. Setting trajectory = hill gives a quadratic.

**Output of `Task_12_modified.py`:**
```text
=== PART 1: Parameter changes ===
radius 2.0:
   guess [1.0, 1.0] -> (1.5175, 1.3028)  converged=True  residual norm=3.5e-13
   guess [-1.0, 1.0] -> (-1.5175, 1.3028)  converged=True  residual norm=3.5e-13
radius 3.0:
   guess [1.0, 1.0] -> (1.8364, 2.3723)  converged=True  residual norm=2.0e-12
   guess [-1.0, 1.0] -> (-1.8364, 2.3723)  converged=True  residual norm=2.0e-12
radius 0.5:
   guess [1.0, 1.0] -> (0.5005, -0.4997)  converged=False  residual norm=3.5e-01
   guess [-1.0, 1.0] -> (-0.5005, -0.4997)  converged=False  residual norm=3.5e-01

=== PART 2: Ball thrown at a hillside ===
Polynomial roots of the intersection equation: [49.581  0.   ]
Ball lands at x = 49.58 m, height y = 12.40 m on the hill
scipy.optimize.root check (guess 45, 11): x=49.58, y=12.40, converged=True
Different guess (2, 0.5) finds the other root: x=0.00, y=0.00 (the launch point itself)
Flight path x (m): [ 0.  12.4 24.8 37.2 49.6] -> y (m): [ 0.   11.85 17.87 18.05 12.4 ]
```
**Interpretation:** `np.roots` gives x = 0 (launch) and x = 49.58 m, where the ball lands at height 12.40 m. `scipy.optimize.root` agrees from a good guess (45, 11), but from a guess near the origin it returns the launch point: nonlinear solvers find the root nearest the initial guess.

