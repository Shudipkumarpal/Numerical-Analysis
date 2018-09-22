import matplotlib.pyplot as plt
import numpy as npm

def f(x):
    result = (x**3)-x-4
    return result
def d_f(x):
    result = 3*(x**2)-1
    return result

def appox_relative_error(current, previous):
    val = abs((current-previous)/current)*100
    return val
root_val = 0
previous_root_val = 2
Es = 0.5
Ea = 100
step = 0
while(Ea>Es):
    step = step +1
    root_val = previous_root_val-(f(previous_root_val)/d_f(root_val))
    Ea = appox_relative_error(root_val, previous_root_val)
    previous_root_val = root_val
print(root_val,'--------',step)
plt.title("newton Raphson")
plt.xlabel("X----------")
plt.ylabel("f(X)----------")
val_x = npm.linspace(1,2,100)
plt.plot(val_x,f(val_x),'b')
plt.plot(root_val,f(root_val),'ro')
plt.show()