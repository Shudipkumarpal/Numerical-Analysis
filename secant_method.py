import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return ((x * x * x) - 20)

def app_err(c, p):
    return ((abs(c - p) / c) * 100)

def secant_m(c_r, p_r):
    return c_r - ((f(c_r) * (c_r - p_r)) / (f(c_r) - f(p_r)))

a = 2
b = 3
Ea = app_err(a, b)
Es = 0.05
count = 0

while(1):
    if(Es > Ea): break
    count = count + 1
    root_val = secant_m(a, b)
    a = b
    b = root_val
    Ea = app_err(a, b)
    
print("Root Value: " ,root_val, "\nSteps needed: " ,count)
val_x = np.linspace(2, 3, num = 100)
plt.plot(val_x, f(val_x), 'g')
plt.plot(root_val, f(root_val), 'ro')
plt.show()