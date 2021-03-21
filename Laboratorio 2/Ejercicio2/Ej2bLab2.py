# min 100(x1 − x20 )2 + (1 − x0 )2
# x0 + 2x1 ≤1,
# x20 + x1 ≤1,
# x0 − x1 ≤4,
# x ∈ Z.
from gekko import GEKKO
m = GEKKO(remote=False)
x1 = m.Var(lb=0,ub=None,integer=True)
x0 = m.Var(lb=0,ub=None,integer=True)

m.Equation(x0 + 2*x1 <= 1)
m.Equation(x0**2 + x1 <= 1)
m.Equation(x0 - x1 <= 4)
m.Obj(100*(x1 - x0**2)**2 + (1-x0)**2)
m.solve(disp=True)
print(f"x0 {x0.value}")
print(f"x1 {x1.value}")