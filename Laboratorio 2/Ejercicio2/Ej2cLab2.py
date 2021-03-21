# min 4x21 − x30
# 3x0 + 2x1 ≤ 17,
# x20 + x21 ≤ 100,
# x20 − 2x1 ≤ 80,
# x ∈ Z.
from gekko import GEKKO
m = GEKKO(remote=False)
x1 = m.Var(lb=0,ub=None,integer=True)
x0 = m.Var(lb=0,ub=None,integer=True)

m.Equation(3*x0 + 2*x1 <= 17)
m.Equation(x0**2 + x1**2 <= 100)
m.Equation(x0**2 - x1 <= 80)
m.Obj(4*x1**2 - x0**3)
m.solve(disp=False)
print(f"x0 {x0.value}")
print(f"x1 {x1.value}")