# Task 11: Root Finding: Newton-Raphson and Secant Methods

*Programs:* `code/Task_11_newton_secant.py` (original) and `code/Task_11_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Cash flows −10000, 3000, 3500, 4000, 2500 (years 0–4). f(r) = NPV(r) with analytical derivative. Newton: r ← r − f/f′. Secant uses two starting rates (5% and 20%) instead of the derivative.

## 2. Original output and its meaning
```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
Newton iterations: 4 | Secant iterations: 7
```
The internal rate of return is 11.542461%: discounting the cash flows at that rate makes NPV zero (NPV ≈ 0). Newton needs 4 iterations, secant 7: both are far faster than bisection.

## 3. Parameter change and how the result changes
With weaker inflows (2000, 2500, 3000, 2000, total 9500 < 10000) the IRR is negative (−2.0%). Starting Newton at 0, 0.10 and 0.50 gives the same IRR, but starting at 1.0 converges to a meaningless root of −154%: Newton can land on a different (spurious) root if the start is far away.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** A loan of KES 100,000 repaid with 12 monthly payments of KES 9,000. The monthly rate r solves 9000·(1 − (1+r)^−12)/r = 100000; the derivative is approximated numerically. Figures are illustrative.

**Output of `Task_11_modified.py`:**
```text
=== PART 1: Parameter changes ===
original        IRR = 11.5425% (Newton, 4 iterations)
weaker inflows  IRR = -2.0012% (Newton, 5 iterations)
start x0=0.00: root=11.542461%, iterations=6
start x0=0.10: root=11.542461%, iterations=4
start x0=0.50: root=11.542461%, iterations=8
start x0=1.00: root=-154.411050%, iterations=7

=== PART 2: Loan - find the monthly rate r ===
Monthly rate (Newton): 1.204346% in 4 iterations
Monthly rate (Secant): 1.204346% in 6 iterations
Annual nominal rate  : 14.452%
Effective annual rate: 15.449%
Total repaid: KES 108,000 (interest paid KES 8,000)
Check f(root) = -1.28e-09
```
**Interpretation:** Monthly rate 1.2043% (Newton in 4 steps, secant in 6), i.e. 14.45% nominal and 15.45% effective per year; total interest KES 8,000. The effective rate is higher than the nominal because of monthly compounding.

