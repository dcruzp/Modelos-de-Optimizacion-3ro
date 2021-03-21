import numpy as np
from pulp import *

n = 3                               #Cantidad de lineas 
b = np.array([14, 17, 16])          #Cantidad de omnibus en las lineas
c = np.array([12000, 21000, 15000]) #Cantidad de pasageros transportados


#Modelo:
model = LpProblem('Terminal N.O', LpMaximize)

#Variables de desicion:
var_name = [str(i) for i in range(n)]

var_temp = LpVariable.matrix('x', var_name, cat='Integer', lowBound=0)
x = np.array(var_temp).reshape(3)

var_temp = LpVariable.matrix('d', var_name, cat='Binary', lowBound=0)
d = np.array(var_temp).reshape(3)

#Funcion objetiva:
fun_obj = lpSum(c*x)
model += fun_obj

#Restricciones:
model += lpSum(x) <= 35
for i in range(n):
    model += x[i] == b[i]*d[i]
    model += x[i] >= 0
    model += d[i] in [0, 1]

model.solve()
model_status = LpStatus[model.status]

print('Model: ', model)
print(model_status)
print('Result:', model.objective.value())
for var in model.variables():
    try:
        print(var.name, '=', var.value())
    except:
        print('Error: Couldn\'t find value')


