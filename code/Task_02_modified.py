"""Task 2 (modified): NumPy arrays.
PART 1 - parameter change: one extreme reading in the weather-station data.
PART 2 - new case: solar-panel output from an IoT inverter (24 hourly kW values)."""
import numpy as np

print("=== PART 1: Parameter change (max reading 29.4 C -> 45.0 C) ===")
base = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
                 29.4, 29.1, 28.5, 27.6, 26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
spike = base.copy()
spike[12] = 45.0                       # one faulty/extreme sensor reading
for name, arr in [("original", base), ("with spike", spike)]:
    print(f"{name:11s} mean={arr.mean():.2f}  median={np.median(arr):.2f}  max={arr.max():.2f}")

print("\n=== PART 2: Solar-panel output (kW, hourly, 00:00-23:00) ===")
solar_kw = np.array([0, 0, 0, 0, 0, 0.1, 0.6, 1.5, 2.6, 3.5, 4.1, 4.4,
                     4.5, 4.3, 3.8, 3.0, 2.0, 0.9, 0.2, 0, 0, 0, 0, 0])
hours = np.arange(24)
energy_kwh = solar_kw.sum() * 1.0       # each reading represents 1 hour
print(f"Total energy generated: {energy_kwh:.1f} kWh")
print(f"Peak output: {solar_kw.max():.1f} kW at hour {hours[solar_kw.argmax()]}:00")
print(f"Hours producing > 3 kW: {hours[solar_kw > 3].tolist()}")
print(f"Daylight hours (output > 0): {(solar_kw > 0).sum()}")
print(f"Average output during daylight: {solar_kw[solar_kw > 0].mean():.2f} kW")
cost_saved = energy_kwh * 25            # assumed tariff: KES 25 per kWh
print(f"Estimated saving at KES 25/kWh: KES {cost_saved:,.0f}")
