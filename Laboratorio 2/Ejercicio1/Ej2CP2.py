import numpy as np
from pulp import *

n = 2        #Cantidad de productos(Quesos)
a = [2.5, 2] #L requeridos por producto
b = [1, 1.5] #Costo al producir 
c = [4, 5]   #Ganancia del producto

#Modelo:
model = LpProblem('Quesos', LpMaximize)

#Variables de desicion:
var_name = [str(i) for i in range(n)]

var_temp = LpVariable.matrix('x', var_name, cat='Integer', lowBound=0)
x = np.array(var_temp).reshape(2)

var_temp = LpVariable.matrix('d', var_name, cat='Binary', lowBound=0)
d = np.array(var_temp).reshape(2)

#Funcion objetiva:
fun_obj = lpSum(c*x)
model += fun_obj

#Restricciones:
model += lpSum(a*x) <= 2000
model += lpSum(b*x) + 500*lpSum(d) <= 1500
for i in range(n):
    model += x[i] <= 2000*d[i]
    model += x[i] >= 0
    model += d[i] in [0,1]

model.solve()
model_status = LpStatus[model.status]

print('Model: ', model)
print(model_status)
print('Result:', model.objective.value())

for var in model.variables():
    try:
        print(var.name , '=' , var.value())
    except:
        print('Error: Couldn\'t find value')
