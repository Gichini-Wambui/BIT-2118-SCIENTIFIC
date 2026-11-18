# Task 4: Floating-Point Arithmetic and Numerical Errors

*Programs:* `code/Task_04_numerical_errors.py` (original) and `code/Task_04_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
0.1 + 0.2 versus 0.3; √2 versus 1.414; and the expression (√(1+x) − 1)/x for tiny x compared with the algebraically equal 1/(√(1+x)+1). Operations: equality test, `np.isclose`, absolute error |true − approx|, relative error abs/|true|.

## 2. Original output and its meaning
```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```
`0.1 + 0.2` is 0.30000000000000004, so exact `==` is False but `np.isclose` is True. Absolute error of 1.414 is 0.00021356 (0.0151% relative). For the unstable formula, subtracting nearly equal numbers (√(1+x) ≈ 1) loses digits (cancellation): at x = 1e-12 the direct result is 0.50004445 whereas the true value is 0.5. The rewritten (stable) formula stays correct.

## 3. Parameter change and how the result changes
I replaced the approximation 1.414 by 1.4142 and 1.41421356: relative error fell from 1.5e-4 to 9.6e-6 and 1.7e-9. Using a very strict tolerance (`rtol=0, atol=1e-20`) made `isclose(0.1+0.2, 0.3)` False, showing that the 'right' answer depends on the tolerance you choose.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** A bank system accumulates a 0.10 KES fee one million times. The exact total is KES 100,000.00. Compared: naive float addition, `math.fsum`, `Decimal`, and integer cents.

**Output of `Task_04_modified.py`:**
```text
=== PART 1: Parameter change ===
approx=1.414       abs error=2.136e-04  relative error=1.510e-04
approx=1.4142      abs error=1.356e-05  relative error=9.590e-06
approx=1.41421356  abs error=2.373e-09  relative error=1.678e-09
isclose(0.1+0.2, 0.3) default tolerance : True
isclose with rtol=0, atol=1e-20 (strict): False

=== PART 2: Accumulated error in banking ===
Naive float loop total : 100000.00000133288
math.fsum total        : 100000.0
Decimal total          : 100000.00
Naive absolute error   : 1.332883e-06
Naive total == 100000? : False
np.isclose to 100000?  : True
Cents-as-integers total: 100000.0
```
**Interpretation:** The naive loop gives 100000.00000133288 (error ≈1.3e-6), so `== 100000` is False even though the error is tiny. `math.fsum`, `Decimal` and integer cents are exact. For money, use integer cents or `Decimal`, and compare floats with a tolerance. Errors accumulate with the number of operations.

