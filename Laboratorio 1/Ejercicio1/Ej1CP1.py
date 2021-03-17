from scipy import optimize

# Lab 1 Ej 1

x0 = [1000, 1000, 1000]

# params
h = [10, 15, 12]
p = [80, 75, 86]
n = [5, 8, 7]
r = [2, 1.5, 1.0]


# func
def target(x, *args) -> float:
    result = 0
    for elem in range(0, 3):
        result += x[elem] * (args[0][elem]) * (args[1][elem]) * (args[3][elem]) - x[elem] * (args[1][elem]) - 5 * x[elem] * (
        args[0][elem]) * (args[2][elem])

    constr_1_value = 0
    for elem in range(0, 3):
        constr_1_value += x[elem] * (args[0][elem]) * (args[2][elem])

    constr_2_value = 0
    for elem in range(0, 3):
        constr_2_value += x[elem] * (args[0][elem])

    if constr_1_value <= 450 and constr_2_value <= 1200:
        print(f"restr_1 value ----> {constr_1_value}, upperbound ----> 450")
        print(f"restr_2 value ----> {constr_2_value}, upperbound ----> 1200")
        print(f"guessing --> {x}\n")
        print(f"target function value for current guessing --> {result}\n")

    return -result


# restrictions
lin_constr = optimize.LinearConstraint([[h[elem] * n[elem] for elem in range(0, 3)], [h[elem] for elem in range(0, 3)]],
                                       [0, 0], [450, 1200])
limits = optimize.Bounds([0, 0, 0], [1200, 1200, 1200])

# solution
res = optimize.minimize(target, x0, args=(h, p, n, r), method='trust-constr', bounds=limits, constraints=[lin_constr])
for i in range(0, 3):
    print(f"x[{i}] = {round(res.x[i])}")