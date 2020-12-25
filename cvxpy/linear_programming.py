import cvxpy as cp 
import numpy as np

##vectors##
#x is the temperature at time t
#d is the gap of temperature x[t+1] - x[t] #pt is the cost of energy use for time t to t+1 d = cp.Variable(24, integer=True)
x = cp.Variable(24, integer=True)
pt = np.random.randn(24)

##parameters##
#dec means drop of temperature per hour
#w means electric energy needed to increase temperature by 1 celcius dec = cp.Parameter(nonneg=True, value=1)
w = cp.Parameter(nonneg=True, value = 0.77)

for i in range(24):
    if i >= 0 and i < 9:
        pt[i]= 53.8 * w 
    elif i >= 9 and i < 10:
        pt[i] = 93.0 * w
    elif i >= 10 and i < 12:
        pt[i] = 131.7 * w 
    elif i >= 12 and i < 17:
        pt[i] = 93.0 * w
    elif i >= 17 and i < 20:
        pt[i] = 131.7 * w 
    elif i >= 20 and i < 22:
        pt[i] = 93.0 * w
    elif i >= 22 and i < 23:
        pt[i] = 131.7 * w 
    elif i >= 23 and i < 25:
        pt[i] = 53.8 * w

objective = (d + dec)*pt
constraints = [x[0] == 19, x >= 19, x <= 25, d <=2, d >=-dec] 

for i in range(23):
    constraints += [x[i+1] - x[i] <= 2, x[i+1] - x[i] == d[i]]

prob = cp.Problem(cp.Minimize(objective), constraints)

try: 
    prob.solve()
except Exception as e: 
    print(e)
