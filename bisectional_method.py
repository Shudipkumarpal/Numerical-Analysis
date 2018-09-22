import matplotlib.pyplot as plt
import numpy as npm

def f(x):
    result = (x**2)-x-1
    return result
def bisectional(a,b):
    return (a+b)/2
def appox_relative_error(current, previous):
    val = abs((current-previous)/current)*100
    return val
a=1 
b=2
previous_root_val = 0
Es = 0.5
n =0
if(f(a)*f(b)<0):
    while(1):
        root_val = bisectional(a,b)
        Ea = appox_relative_error(a,b)
        if(f(a)*f(root_val)<0):
            b = root_val
        elif (f(a)*f(root_val)>0):
            a = root_val
        elif(f(a)*f(root_val)==0):
            break
        elif(Ea<=Es):
            break
        previous_root_val = root_val
        print(root_val)
    val_x = npm.linspace(1,2,100)
    plt.plot(val_x,f(val_x),'b')
    plt.plot(root_val,f(root_val),'ro')
    plt.show()