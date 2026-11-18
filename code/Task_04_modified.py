"""Task 4 (modified): floating-point errors.
PART 1 - parameter change: a better approximation of sqrt(2) and a stricter tolerance.
PART 2 - new case: a banking system adding 0.10 KES one million times."""
import math
import numpy as np
from decimal import Decimal

print("=== PART 1: Parameter change ===")
true_value = np.sqrt(2)
for approx in (1.414, 1.4142, 1.41421356):
    abs_err = abs(true_value - approx)
    print(f"approx={approx:<11} abs error={abs_err:.3e}  relative error={abs_err/true_value:.3e}")
print("isclose(0.1+0.2, 0.3) default tolerance :", np.isclose(0.1 + 0.2, 0.3))
print("isclose with rtol=0, atol=1e-20 (strict):", np.isclose(0.1 + 0.2, 0.3, rtol=0, atol=1e-20))

print("\n=== PART 2: Accumulated error in banking ===")
n = 1_000_000
naive = 0.0
for _ in range(n):
    naive += 0.10                      # float: 0.1 is not exactly representable
exact_total = 100_000.00
print(f"Naive float loop total : {naive!r}")
print(f"math.fsum total        : {math.fsum([0.10] * n)!r}")
print(f"Decimal total          : {sum(Decimal('0.10') for _ in range(n))}")
print(f"Naive absolute error   : {abs(naive - exact_total):.6e}")
print(f"Naive total == 100000? : {naive == exact_total}")
print(f"np.isclose to 100000?  : {np.isclose(naive, exact_total)}")
print(f"Cents-as-integers total: {sum([10] * n) / 100}")
