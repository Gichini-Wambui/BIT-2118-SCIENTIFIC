"""Task 11 (modified): Newton-Raphson and secant.
PART 1 - parameter change: weaker cash inflows, and different starting guesses.
PART 2 - new case: the monthly interest rate hidden in a loan (KES 100,000 repaid as 12 x KES 9,000)."""
from scipy.optimize import root_scalar

print("=== PART 1: Parameter changes ===")
def make(cf):
    npv = lambda r: sum(c / (1 + r) ** t for t, c in enumerate(cf))
    dnpv = lambda r: sum(-t * c / (1 + r) ** (t + 1) for t, c in enumerate(cf) if t > 0)
    return npv, dnpv
for label, cf in (("original", [-10000, 3000, 3500, 4000, 2500]),
                  ("weaker inflows", [-10000, 2000, 2500, 3000, 2000])):
    npv, dnpv = make(cf)
    s = root_scalar(npv, fprime=dnpv, x0=0.10, method="newton", xtol=1e-12)
    print(f"{label:15s} IRR = {s.root:.4%} (Newton, {s.iterations} iterations)")
npv, dnpv = make([-10000, 3000, 3500, 4000, 2500])
for x0 in (0.0, 0.10, 0.50, 1.0):
    try:
        s = root_scalar(npv, fprime=dnpv, x0=x0, method="newton", xtol=1e-12)
        print(f"start x0={x0:4.2f}: root={s.root:.6%}, iterations={s.iterations}")
    except Exception as e:
        print(f"start x0={x0:4.2f}: failed ({type(e).__name__})")

print("\n=== PART 2: Loan - find the monthly rate r ===")
P, pmt, n = 100_000, 9_000, 12
f = lambda r: pmt * (1 - (1 + r) ** (-n)) / r - P            # present value of payments minus amount borrowed
def df(r, h=1e-8):                                           # derivative approximated numerically
    return (f(r + h) - f(r - h)) / (2 * h)
newton = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.01, x1=0.05, method="secant", xtol=1e-12)
print(f"Monthly rate (Newton): {newton.root:.6%} in {newton.iterations} iterations")
print(f"Monthly rate (Secant): {secant.root:.6%} in {secant.iterations} iterations")
print(f"Annual nominal rate  : {newton.root * 12:.3%}")
print(f"Effective annual rate: {(1 + newton.root) ** 12 - 1:.3%}")
print(f"Total repaid: KES {pmt * n:,} (interest paid KES {pmt * n - P:,})")
print(f"Check f(root) = {f(newton.root):.2e}")
