"""Task 19: optimization.
PART 1 - parameter change: cost of Type A lowered to 9, and capacity requirement raised to 1500.
PART 2 - new case: cheapest fertiliser mix that supplies at least 120 kg N and 80 kg P (with a 150 kg cap on total bags)."""
import numpy as np
from scipy.optimize import minimize

def solve(cost_a=12, cost_b=18, need=1000):
    res = minimize(lambda z: cost_a*z[0] + cost_b*z[1], x0=[5, 3], method="SLSQP", bounds=[(0, None)]*2,
                   constraints={"type": "ineq", "fun": lambda z: 100*z[0] + 170*z[1] - need})
    return res

print("=== PART 1: Parameter changes ===")
print("cost per capacity unit: A =", 12/100, " B =", round(18/170, 4))
for label, kw in (("original (12, 18, 1000)", {}), ("Type A cost 9", {"cost_a": 9}), ("capacity 1500", {"need": 1500})):
    r = solve(**kw)
    print(f"{label:24s} A={r.x[0]:7.3f} B={r.x[1]:7.3f} cost={r.fun:8.2f}")

print("\n=== PART 2: Fertiliser mix ===")
# Per bag of 50 kg: product X gives 20 kg N / 5 kg P, costs 3200 KES; product Y gives 6 kg N / 12 kg P, costs 3600 KES
cost = lambda z: 3.2*z[0] + 3.6*z[1]          # cost in thousands of KES (scaling helps SLSQP)
cons = [{"type": "ineq", "fun": lambda z: 20*z[0] + 6*z[1] - 120},     # nitrogen >= 120 kg
        {"type": "ineq", "fun": lambda z: 5*z[0] + 12*z[1] - 80},      # phosphorus >= 80 kg
        {"type": "ineq", "fun": lambda z: 150 - z[0] - z[1]}]          # at most 150 bags
r = minimize(cost, x0=[10, 10], method="SLSQP", bounds=[(0, None)]*2, constraints=cons)
x, y = r.x
print("Success:", r.success)
print(f"Bags of X: {x:.3f}, bags of Y: {y:.3f}, minimum cost: KES {r.fun*1000:,.0f}")
print(f"Nitrogen supplied: {20*x + 6*y:.1f} kg (need 120) | Phosphorus supplied: {5*x + 12*y:.1f} kg (need 80)")
best = None
for a in range(0, 40):
    for b in range(0, 40):
        if 20*a + 6*b >= 120 and 5*a + 12*b >= 80 and a + b <= 150:
            c = 3200*a + 3600*b
            if best is None or c < best[0]: best = (c, a, b)
print(f"Best whole-bag solution: cost={best[0]:,}, X={best[1]}, Y={best[2]}, N={20*best[1]+6*best[2]}, P={5*best[1]+12*best[2]}")
