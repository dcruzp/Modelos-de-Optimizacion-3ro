from scipy import optimize

#Lab 1 Ej 2
def rosenbrock (x) -> float:
    return sum(100*(x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# Cuando n = 2
x_2 = [2.1, 3.5] # valores de los x_i
res = optimize.minimize(rosenbrock, x_2, method='nelder-mead', options={'xatol': 1e-8, 'disp': False})
print(res.x)

# Cuando n = 3
x_3 = [2.1, 3.5, 0.9] # valores de los x_i
res = optimize.minimize(rosenbrock, x_3, method='nelder-mead', options={'xatol': 1e-8, 'disp': False})
print(res.x)

# Cuando n = 4
x_4 = [2.1, 3.5, 0.9, 4.2] # valores de los x_i
res = optimize.minimize(rosenbrock, x_4, method='nelder-mead', options={'xatol': 1e-8, 'disp': False})
print(res.x)

# Cuando n = 5
x_5 = [2.1, 3.5, 0.9, 4.2, 1.7] # valores de los x_i
res = optimize.minimize(rosenbrock, x_5, method='nelder-mead', options={'xatol': 1e-8, 'disp': False})
print(res.x)