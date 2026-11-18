# BIT 2118 Scientific Computing: Group Work Portfolio

Student name: GICHINI LOISE WAMBUI  
Reg. No: BSCCS/2025/40219 

Task 1 (Data Science Essentials with Python) is the self-paced prerequisite and has no program. Tasks 2-20 each have:

- the original program from the brief (`code/Task_XX_*.py`);
- a modified program (`code/Task_XX_modified.py`) with **Part 1**, a changed input/parameter, and **Part 2**, a different real-world case;
- a document (`docs/Task_XX.md`) covering the inputs and operation, the meaning of the output, the effect of the parameter change, and the new case's assumptions, input data, output and interpretation.

| Task | Topic | Documentation | Original program | Modified program |
|---|---|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | [docs/Task_02.md](docs/Task_02.md) | `code/Task_02_numpy_arrays.py` | `code/Task_02_modified.py` |
| 3 | Mathematical Functions and Vectorization | [docs/Task_03.md](docs/Task_03.md) | `code/Task_03_vectorization.py` | `code/Task_03_modified.py` |
| 4 | Floating-Point Arithmetic and Numerical Errors | [docs/Task_04.md](docs/Task_04.md) | `code/Task_04_numerical_errors.py` | `code/Task_04_modified.py` |
| 5 | Matrix Algebra and Matrix Operations | [docs/Task_05.md](docs/Task_05.md) | `code/Task_05_matrix_algebra.py` | `code/Task_05_modified.py` |
| 6 | Solution of Systems of Linear Equations | [docs/Task_06.md](docs/Task_06.md) | `code/Task_06_linear_systems.py` | `code/Task_06_modified.py` |
| 7 | Gaussian Elimination and LU Decomposition | [docs/Task_07.md](docs/Task_07.md) | `code/Task_07_gaussian_lu.py` | `code/Task_07_modified.py` |
| 8 | Iterative Methods for Linear Systems | [docs/Task_08.md](docs/Task_08.md) | `code/Task_08_iterative_linear.py` | `code/Task_08_modified.py` |
| 9 | Eigenvalues and Eigenvectors | [docs/Task_09.md](docs/Task_09.md) | `code/Task_09_eigenvalues.py` | `code/Task_09_modified.py` |
| 10 | Root Finding: Bisection and Fixed-Point | [docs/Task_10.md](docs/Task_10.md) | `code/Task_10_bisection_fixed_point.py` | `code/Task_10_modified.py` |
| 11 | Root Finding: Newton-Raphson and Secant | [docs/Task_11.md](docs/Task_11.md) | `code/Task_11_newton_secant.py` | `code/Task_11_modified.py` |
| 12 | Polynomial and Nonlinear Equation Solving | [docs/Task_12.md](docs/Task_12.md) | `code/Task_12_nonlinear_equations.py` | `code/Task_12_modified.py` |
| 13 | Interpolation | [docs/Task_13.md](docs/Task_13.md) | `code/Task_13_interpolation.py` | `code/Task_13_modified.py` |
| 14 | Curve Fitting and Approximation | [docs/Task_14.md](docs/Task_14.md) | `code/Task_14_curve_fitting.py` | `code/Task_14_modified.py` |
| 15 | Numerical Differentiation | [docs/Task_15.md](docs/Task_15.md) | `code/Task_15_numerical_differentiation.py` | `code/Task_15_modified.py` |
| 16 | Numerical Integration | [docs/Task_16.md](docs/Task_16.md) | `code/Task_16_numerical_integration.py` | `code/Task_16_modified.py` |
| 17 | ODEs - Euler Method | [docs/Task_17.md](docs/Task_17.md) | `code/Task_17_euler_ode.py` | `code/Task_17_modified.py` |
| 18 | ODEs Using SciPy | [docs/Task_18.md](docs/Task_18.md) | `code/Task_18_scipy_ode.py` | `code/Task_18_modified.py` |
| 19 | Numerical Optimization | [docs/Task_19.md](docs/Task_19.md) | `code/Task_19_optimization.py` | `code/Task_19_modified.py` |
| 20 | Random Numbers and Monte Carlo Methods | [docs/Task_20.md](docs/Task_20.md) | `code/Task_20_monte_carlo.py` | `code/Task_20_modified.py` |

## Running the code
```bash
pip install -r requirements.txt
cd code
python Task_02_numpy_arrays.py      # run any task from inside the code/ folder
```
Programs that draw graphs save a PNG in `figures/` and also call `plt.show()`. `np.trapezoid` (Task 16) needs NumPy 2.0 or later. Timing results (Tasks 3 and 7) depend on your computer.

## Notes on changes to the original programs
- Task 13: the 10-minute time grid is clipped to the data range, since `np.arange` with a 1/6 step can overshoot 14.0 and `interp1d` rejects it.
- Task 16: the f-string that was split across lines in the PDF was joined.
- Tasks 8, 10, 13-15, 17, 18, 20: added a `plt.savefig` call and, in a few, an extra iteration-count print.


