import numpy as np
from scipy.optimize import minimize
from pulp import LpProblem, LpMaximize, LpMinimize, LpVariable, lpSum, LpStatus

def L1_E3(n, m, l, c, a, b, d, D):
    model = LpProblem('Bodegas', LpMinimize)

    # Variables de decisiones.
    var_name = [str(i) + str(j) for i in range(1, n + 1) for j in range(1, m + 1)]
    var_name.sort()
    var_temp = LpVariable.matrix('x', var_name, cat='Integer', lowBound=0)
    x = np.array(var_temp).reshape(2, 5)

    # Funcion objetiva:
    fun_obj = lpSum(lpSum(c[j] * x[i][j] for j in range(m)) for i in range(n)) - lpSum(c[j] * d[j] for j in range(m))
    model += fun_obj

    # Restrinciones:
    for i in range(n):
        for k in range(l):
            model += lpSum(x[i][j] * a[j][k] for j in range(m)) == lpSum(x[i][j] * b[i][k] for j in range(m))
    for j in range(m):
        model += lpSum(x[i][j] for i in range(n)) >= d[j]
    for i in range(n):
        model += lpSum(x[i][j] for j in range(m)) >= D[i]
    for i in range(n):
        for j in range(m):
            model += x[i][j] >= 0

    model.solve()
    model_status = LpStatus[model.status]

    print('Modelo:', model)
    print(model_status)
    print('Ganancia total: ', model.objective.value())
    print('Variables de desiciones:')
    for var in model.variables():
        try:
            print(var.name, '=', var.value())
        except:
            print('Error: Couldn\'t find value')


# Lab 1 Ex 3
n, m, l = 2, 5, 3  # Cantidad de productos, mezcla y MP
c = [3.20, 2.20, 3.80, 2.60, 1.20]  # Precio de las mezclas
a = [[0.7, 0.1, 0.2],
     [0.4, 0.0, 0.6],
     [1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 1.0]]  # Composicion de cada mezcla
b = [[0.8, 0.1, 0.1],
     [0.55, 0.15, 0.3]]  # Composicion requerida
d = [500, 150, 0, 0, 0]  # Mezcal disponible
D = [550, 420]  # Demanda del producto

L1_E3(n, m, l, c, a, b, d, D)