from scipy import optimize
import numpy as np
from scipy.optimize.optimize import rosen

#Lab 1 Ej 3

def non_linear_constr (x):
    return [x[0]**2 + x[1]]

def constr_Hess(x, t):
    return t[0]*np.array([[2, 0]])

def constr_Jac(x):
    return [[2*x[0], 1]]

def rosenbrock (x) -> float:
    return sum(100*(x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

x0 = [2, 3]

lin_constr = optimize.LinearConstraint([[1, 2], [1, -1]], [-np.inf,  -np.inf], [1, 4])
nonlin_constr = optimize.NonlinearConstraint(non_linear_constr, -np.inf, 1, jac = constr_Jac, hess = constr_Hess)

res = optimize.minimize(rosenbrock, x0, method = 'trust-constr', constraints = [lin_constr, nonlin_constr], options = {'verbose' : 0})
print(res.x)