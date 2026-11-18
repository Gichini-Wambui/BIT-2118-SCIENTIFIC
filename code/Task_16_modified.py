"""Task 16: numerical integration.
PART 1 - parameter change: number of sample points on a known integral (trapezoid vs Simpson).
PART 2 - new case: volume of water delivered by a borehole pump from flow-rate readings."""
import numpy as np
from scipy.integrate import simpson, quad

print("=== PART 1: Effect of the number of intervals, integral of sin(x) from 0 to pi (exact = 2) ===")
print(f"{'intervals':>9} {'trapezoid err':>14} {'simpson err':>13}")
for n in (2, 4, 8, 16, 32):
    x = np.linspace(0, np.pi, n + 1)
    y = np.sin(x)
    print(f"{n:9d} {abs(np.trapezoid(y, x) - 2):14.3e} {abs(simpson(y, x=x) - 2):13.3e}")
print("Original smart-meter data with readings every 4 h instead of 2 h:")
t = np.array([0, 2, 4, 6, 8, 10, 12.]); p = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
print(f"   every 2 h: trapezoid={np.trapezoid(p, t):.3f}, Simpson={simpson(p, x=t):.3f} kWh")
print(f"   every 4 h: trapezoid={np.trapezoid(p[::2], t[::2]):.3f}, Simpson={simpson(p[::2], x=t[::2]):.3f} kWh")

print("\n=== PART 2: Water delivered by a borehole pump ===")
minutes = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)
flow_lps = np.array([0.0, 2.1, 2.8, 3.0, 2.9, 2.4, 1.0])                  # litres per second
seconds = minutes * 60
vol_trap = np.trapezoid(flow_lps, seconds)
vol_simp = simpson(flow_lps, x=seconds)
print(f"Volume (trapezoid): {vol_trap:,.0f} litres")
print(f"Volume (Simpson)  : {vol_simp:,.0f} litres")
print(f"Difference: {abs(vol_trap - vol_simp):,.0f} litres ({abs(vol_trap - vol_simp)/vol_simp:.2%})")
print(f"Average flow rate: {vol_simp / seconds[-1]:.2f} L/s")
print(f"Number of 20-litre jerrycans filled: {vol_simp / 20:,.0f}")
