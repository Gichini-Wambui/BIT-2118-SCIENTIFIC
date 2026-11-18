"""Task 18: solve_ivp.
PART 1 - parameter change: resistance R doubled, and tolerance loosened.
PART 2 - new case: SIR epidemic model for a school of 1,000 pupils."""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

print("=== PART 1: Parameter changes (RC circuit) ===")
Vs, C = 5.0, 0.001
for R in (1000.0, 2000.0):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / (R * C)], (0, 5), [0.0], t_eval=np.linspace(0, 5, 200), rtol=1e-9, atol=1e-11)
    tau = R * C
    print(f"R={R:6.0f} ohm: tau={tau:.1f} s  V(1 s)={np.interp(1, sol.t, sol.y[0]):.3f} V  V(5 s)={sol.y[0, -1]:.4f} V")
for rtol in (1e-9, 1e-2):
    sol = solve_ivp(lambda t, V: [(Vs - V[0]) / 1.0], (0, 5), [0.0], t_eval=np.linspace(0, 5, 200), rtol=rtol, atol=rtol)
    ex = Vs * (1 - np.exp(-sol.t))
    print(f"rtol={rtol:g}: function evaluations={sol.nfev}, max error={np.max(abs(sol.y[0]-ex)):.2e} V")

print("\n=== PART 2: SIR epidemic, N = 1000, beta = 0.4/day, gamma = 0.1/day ===")
N, beta, gamma = 1000.0, 0.4, 0.1
def sir(t, y):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]
t_eval = np.linspace(0, 120, 481)
sol = solve_ivp(sir, (0, 120), [995, 5, 0], t_eval=t_eval, rtol=1e-8, atol=1e-10)
S, I, R = sol.y
peak = I.argmax()
print(f"R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infections: {I[peak]:.0f} pupils on day {sol.t[peak]:.1f}")
print(f"Final number ever infected: {R[-1]:.0f} ({R[-1]/N:.1%})")
print(f"Conservation check S+I+R at the end: {S[-1] + I[-1] + R[-1]:.6f}")
sol2 = solve_ivp(lambda t, y: [-0.2*y[0]*y[1]/N, 0.2*y[0]*y[1]/N - gamma*y[1], gamma*y[1]], (0, 120), [995, 5, 0], t_eval=t_eval, rtol=1e-8, atol=1e-10)
print(f"With measures (beta = 0.2, R0 = 2): peak {sol2.y[1].max():.0f}, total infected {sol2.y[2, -1]:.0f}")
plt.plot(sol.t, S, label="Susceptible"); plt.plot(sol.t, I, label="Infected"); plt.plot(sol.t, R, label="Recovered")
plt.plot(sol2.t, sol2.y[1], "--", label="Infected (beta=0.2)")
plt.xlabel("Days"); plt.ylabel("Pupils"); plt.title("SIR epidemic in a school"); plt.legend(); plt.grid(True)
plt.savefig("../figures/task18_modified.png", dpi=120, bbox_inches="tight"); plt.show()
