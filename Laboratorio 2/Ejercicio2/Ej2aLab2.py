# min 3x1 − x0^2
# 3x0 + 2x1 ≤ 50,
# 2x0 + x1 ≤ 30,
# x ∈ Z.

from gekko import GEKKO
m = GEKKO(remote=False)
x1 = m.Var(lb=0,ub=None)
x0 = m.Var(lb=0,ub=None)

m.Equation(3*x0 + 2*x1 <= 50)
m.Equation(2*x0 + x1 <= 30)
m.Obj(3*x1 - x0**2)
m.solve(disp=False)
print(f"x0 {x0.value}")
print(f"x1 {x1.value}")