# Task 2: NumPy Arrays and Numerical Computation

*Programs:* `code/Task_02_numpy_arrays.py` (original) and `code/Task_02_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
24 hourly temperatures (°C) stored in one NumPy array. Operations: arithmetic mean (sum ÷ 24), minimum, maximum, and the vectorised conversion F = 1.8·C + 32 applied to every element at once.

## 2. Original output and its meaning
```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```
The day averaged 23.12 °C, the coolest hour was 17.50 °C (early morning) and the warmest 29.40 °C (early afternoon). The first six Fahrenheit values (about 63.5–66.2 °F) are the converted overnight readings. The shape of the data (cool night, warm afternoon) matches a normal daily temperature cycle.

## 3. Parameter change and how the result changes
I replaced the 12:00 reading (29.4 °C) with an extreme 45.0 °C. The **mean rose from 23.12 to 23.77 °C** and the maximum became 45.0, but the **median stayed 22.75 °C**. One bad reading drags the mean but barely affects the median, so the median is more robust for faulty sensors.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** Solar-panel inverter reports output in kW once per hour. Each reading represents the average power for that hour, so kW × 1 h = kWh. Tariff assumed to be KES 25/kWh (an assumption, change to the real tariff). Data are illustrative.

**Output of `Task_02_modified.py`:**
```text
=== PART 1: Parameter change (max reading 29.4 C -> 45.0 C) ===
original    mean=23.12  median=22.75  max=29.40
with spike  mean=23.77  median=22.75  max=45.00

=== PART 2: Solar-panel output (kW, hourly, 00:00-23:00) ===
Total energy generated: 35.5 kWh
Peak output: 4.5 kW at hour 12:00
Hours producing > 3 kW: [9, 10, 11, 12, 13, 14]
Daylight hours (output > 0): 14
Average output during daylight: 2.54 kW
Estimated saving at KES 25/kWh: KES 888
```
**Interpretation:** Total generation is 35.5 kWh, peaking at 4.5 kW at 12:00, with 14 hours of non-zero output and 6 hours above 3 kW (09:00–14:00). Boolean masks (`solar_kw > 3`) select data without loops. At KES 25/kWh the day is worth about KES 888. The bell shape is typical of solar output.

