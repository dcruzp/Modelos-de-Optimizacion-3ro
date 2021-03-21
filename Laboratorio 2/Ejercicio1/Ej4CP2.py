import numpy as np
from pulp import *

n, m = 5, 5              #Cantidad de cursos y de dias
a = [[3,  2, 3,  4,  9], #Cantidad de estudiantes que
     [0, 10, 5,  8, 10], #no pueden asistir
     [1,  3, 3, 10,  2],
     [6,  1, 1,  0,  5],
     [0,  8, 6,  2,  3]]


 #Modelo:
model = LpProblem('Cursos', LpMinimize)

#Variables de desicion:
var_name = [str(i)+str(j) for i in range(n) for j in range(m)]
var_name.sort()

var_temp = LpVariable.matrix('d', var_name, cat='Binary', lowBound=0)
d = np.array(var_temp).reshape(5,5)

#Funcion objetiva
fun_obj = lpSum(lpSum(a[i][j]*d[i][j] for j in range(m)) for i in range(n))
model += fun_obj

#Restricciones:
for i in range(n):
    model += lpSum(d[i][j] for j in range(m)) == 1
for j in range(m):
    model += lpSum(d[i][j] for i in range(n)) == 1
for i in range(n):
    for j in range(m):
        model += d[i][j] in [0,1]
    
model.solve()
model_status = LpStatus[model.status]

print('Modelo: ', model)
print(model_status)
print('Result:', model.objective.value())

for var in model.variables():
    try: print(var.name , '=' , var.value())
    except:print('Error: Couldn\'t find value')