from pulp import *

model = LpProblem("Producrion Planing", LpMaximize)

x_A = LpVariable('Product_A',0)
x_B = LpVariable('Product_B',0)

model += 2 * x_A + 4 * x_B

model += 3 * x_A + 3 * x_B <= 9
model += x_A + x_B <= 4
model += x_A + x_B * 3 <= 6

model.solve()

print("STATUS:")
print(LpStatus[model.status])
print("OPTIMAL PROD OF A:")
print(value(x_A))
print("OPTIMAL PROD OF B:")
print(value(x_B))
print("TOTAL PROFIT:")
print(value(model.objective))