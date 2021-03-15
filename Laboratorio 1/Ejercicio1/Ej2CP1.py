from scipy import optimize

# Lab 1 Ej 1

x0 = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]

# parametros
b = [2000, 3000, 1500]
a = [6000, 4000, 2000]
p = [6, 8, 5]


# func
def constr_eq_comparer(l: list) -> bool:
    restrs = [0] * 3
    for elem in range(0, 9):
        restrs[elem % 3] += l[elem] / b[elem % 3]

    return restrs[0] == restrs[1] == restrs[2]


def constr_ineq_comparer(l1: list, l2: list) -> bool:
    for i in range(0, 3):
        if l1[i] > l2[i]:
            return False

    return True


def target(x, *args) -> float:
    result = 0
    for i in range(0, 9):
        result += x[i] * p[i % 3]

    constr_1_value = [0] * 3  # restriccion, capacidad de cada almacen (valor actual)
    for elem in range(0, 9):
        constr_1_value[elem % 3] += x[elem]

    constr_2_value = [0] * 3  # restriccion, limite de toneladas de cada producto (valor actual)
    for elem in range(0, 9):
        line = 0 if elem in range(0, 3) else 1 if elem in range(3, 6) else 2
        constr_2_value[line] += x[elem]

    # Ayuda para imprimir aquellos posibles valores de x que cumplan las condiciones
    if constr_ineq_comparer(constr_1_value, b) and constr_ineq_comparer(constr_2_value, a) and constr_eq_comparer(x):
        print(f"restr_1 value ----> {constr_1_value}, upperbound ----> {b}")
        print(f"restr_2 value ----> {constr_2_value}, upperbound ----> {a}")
        print(f"guessing ----> {x}\n")
        print(f"target function value for current guessing ----> {result}\n")

    return -result


# restricciones
constr_1 = optimize.LinearConstraint([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 1, 1, 1]], [0, 0, 0], b)

constr_2 = optimize.LinearConstraint([[1, 0, 0, 1, 0, 0, 1, 0, 0],
                                      [0, 1, 0, 0, 1, 0, 0, 1, 0],
                                      [0, 0, 1, 0, 0, 1, 0, 0, 1]], [0, 0, 0], a)

constr_3 = optimize.LinearConstraint([[1 / b[0], -1 / b[1], 0, 1 / b[0], -1 / b[1], 0, 1 / b[0], -1 / b[1], 0],
                                      [0, -1 / b[1], 1 / b[2], 0, -1 / b[1], 1 / b[2], 0, -1 / b[1], 1 / b[2]]], [0, 0],
                                     [0, 0])

limits = optimize.Bounds([0, 0, 0, 0, 0, 0, 0, 0, 0], [6000, 6000, 6000, 4000, 4000, 4000, 2000, 2000, 2000])

res = optimize.minimize(target, x0, method='trust-constr', bounds=limits, constraints=[constr_1, constr_2, constr_3])
net_worth = 0
for i in range(0, 9):
    line = 0 if i in range(0, 3) else 1 if i in range(3, 6) else 2
    net_worth += res.x[i] * p[line]
    print(f"x[{i}] = {round(res.x[i])}")

print(f"net_worth ----> {net_worth}")
