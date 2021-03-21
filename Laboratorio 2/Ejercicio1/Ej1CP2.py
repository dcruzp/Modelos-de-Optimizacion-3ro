import numpy as np

from pulp import LpProblem, LpMaximize, LpMinimize, LpVariable, lpSum, LpStatus

model = LpProblem('Terminal', LpMinimize)

