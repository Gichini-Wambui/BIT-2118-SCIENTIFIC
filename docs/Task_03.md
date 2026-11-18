# Task 3: Mathematical Functions and Vectorization

*Programs:* `code/Task_03_vectorization.py` (original) and `code/Task_03_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
One million simulated latency values (uniform 5–250 ms, seed 42). Operation: divide by 1000 (ms → s) then square, done once with a Python loop and once with a single NumPy expression, timed with `timeit`.

## 2. Original output and its meaning
```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1468 s
Vectorized time: 0.0027 s
Approximate speed-up: 55.4x
```
Both versions give identical numbers; the vectorised one is much faster (a speed-up of tens of times in my run). The exact times depend on the computer, so your numbers will differ, but the vectorised version should always win by a large factor because the loop runs in interpreted Python while NumPy runs compiled C over a contiguous array.

## 3. Parameter change and how the result changes
I changed the array size N to 100, 10,000 and 1,000,000. Vectorisation was faster at every size (about 16× at N=100, over 100× at N=10,000, and tens of times at one million). The advantage is largest where the loop overhead dominates; at very large N memory traffic limits NumPy. Speed-ups are measured values and vary between runs.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** Mobile-money style fee: 1.5% of the amount, with a minimum fee of KES 10 and a maximum of KES 100. One million simulated amounts uniformly between KES 50 and 20,000 (seed 42). Fee rules are assumptions, not a real tariff.

**Output of `Task_03_modified.py`:**
```text
=== PART 1: Effect of array size (original latency problem) ===
N=      100: loop=0.000012s vectorized=0.000001s speed-up=14.9x
N=   10,000: loop=0.001107s vectorized=0.000011s speed-up=105.1x
N=1,000,000: loop=0.148339s vectorized=0.004896s speed-up=30.3x

=== PART 2: Transaction fees ===
First five amounts: [ 8384.06 18037.65  2198.51 16194.55  7896.39]
First five fees   : [100.   100.    32.98 100.   100.  ]
Total fees collected: KES 83,687,011
Share of transactions at the KES 100 cap: 66.8%
Loop: 0.1301s | Vectorized: 0.0027s | speed-up 48.7x
Results identical: True
```
**Interpretation:** `np.clip` applies the minimum and maximum in a single vectorised call and matches the loop result exactly (`Results identical: True`). About two thirds of transactions hit the KES 100 cap because 1.5% of any amount above ≈KES 6,667 exceeds 100. Total fees ≈ KES 83.7 million; the vectorised version is far faster than the loop.

