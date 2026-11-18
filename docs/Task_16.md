# Task 16: Numerical Integration

*Programs:* `code/Task_16_numerical_integration.py` (original) and `code/Task_16_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Power readings every 2 hours over 12 h. Trapezoid rule (areas of trapezoids) and Simpson's rule (parabolas). Note: the original PDF line splits an f-string across lines; I joined it. `np.trapezoid` requires NumPy ≥ 2.0 (older versions use `np.trapz`).

## 2. Original output and its meaning
```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```
Energy ≈ 15.70 kWh (trapezoid) and 15.80 kWh (Simpson). The difference of 0.10 kWh (0.6%) gives an idea of the numerical uncertainty from the coarse sampling.

## 3. Parameter change and how the result changes
On ∫₀^π sin x dx = 2, doubling the intervals cuts trapezoid error ≈4× and Simpson error ≈16×. With the meter readings every 4 h instead of 2 h, the estimates move to 15.40 (trapezoid) and 15.97 (Simpson), a bigger disagreement: coarse sampling gives a less reliable integral.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** A borehole pump's flow rate (litres/s) is read every 10 minutes for an hour. Volume = ∫ flow dt with time converted to seconds.

**Output of `Task_16_modified.py`:**
```text
=== PART 1: Effect of the number of intervals, integral of sin(x) from 0 to pi (exact = 2) ===
intervals  trapezoid err   simpson err
        2      4.292e-01     9.440e-02
        4      1.039e-01     4.560e-03
        8      2.577e-02     2.692e-04
       16      6.430e-03     1.659e-05
       32      1.607e-03     1.033e-06
Original smart-meter data with readings every 4 h instead of 2 h:
   every 2 h: trapezoid=15.700, Simpson=15.800 kWh
   every 4 h: trapezoid=15.400, Simpson=15.967 kWh

=== PART 2: Water delivered by a borehole pump ===
Volume (trapezoid): 8,220 litres
Volume (Simpson)  : 8,480 litres
Difference: 260 litres (3.07%)
Average flow rate: 2.36 L/s
Number of 20-litre jerrycans filled: 424
```
**Interpretation:** Volume ≈ 8,220 L (trapezoid) or 8,480 L (Simpson), a 3% difference. Average flow 2.36 L/s; about 424 jerrycans of 20 L. Because the flow rises then drops quickly at the end, the quadratic curve of Simpson's rule captures more of the shape; report the result as roughly 8.2–8.5 m³.

