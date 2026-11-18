# Task 19: Numerical Optimization

*Programs:* `code/Task_19_optimization.py` (original) and `code/Task_19_modified.py` (parameter change + new case). Run from inside the `code/` folder.

## 1. Inputs and mathematical operation
Minimise cost 12x + 18y subject to 100x + 170y ≥ 1000 and x, y ≥ 0, using SLSQP from the start (5, 3). Then a brute-force integer search.

## 2. Original output and its meaning
```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```
The optimum is 0 of Type A and 5.882 of Type B, cost 105.88, capacity exactly 1000. Type B is cheaper per capacity unit (0.1059 vs 0.12), so it is chosen alone. If whole servers are required the best nearby solution is 6 B servers: cost 108, capacity 1020.

## 3. Parameter change and how the result changes
Cutting the cost of Type A to 9 (0.09 per capacity unit, now cheaper than B) flips the solution to 10 A and 0 B (cost 90). Raising the capacity requirement to 1500 gives 8.824 B (cost 158.82): the cost scales in proportion to the requirement.

## 4. Modified program: new real-world case
**Assumptions, inputs and data:** Fertiliser planning: minimise cost of bags of product X (20 kg N, 5 kg P, KES 3,200) and Y (6 kg N, 12 kg P, KES 3,600) so that at least 120 kg of nitrogen and 80 kg of phosphorus are supplied, with at most 150 bags. Costs and nutrient contents are illustrative; cost is scaled to thousands of KES for numerical stability.

**Output of `Task_19_modified.py`:**
```text
=== PART 1: Parameter changes ===
cost per capacity unit: A = 0.12  B = 0.1059
original (12, 18, 1000)  A=  0.000 B=  5.882 cost=  105.88
Type A cost 9            A= 10.000 B=  0.000 cost=   90.00
capacity 1500            A=  0.000 B=  8.824 cost=  158.82

=== PART 2: Fertiliser mix ===
Success: True
Bags of X: 4.571, bags of Y: 4.762, minimum cost: KES 31,771
Nitrogen supplied: 120.0 kg (need 120) | Phosphorus supplied: 80.0 kg (need 80)
Best whole-bag solution: cost=34,000, X=5, Y=5, N=130, P=85
```
**Interpretation:** The continuous optimum is 4.571 bags of X and 4.762 bags of Y, cost KES 31,771, meeting both nutrient limits exactly (both constraints are active). With whole bags the best is 5 + 5 bags, KES 34,000, supplying 130 kg N and 85 kg P (slightly over). Integer restrictions raise the cost by about 7%.

