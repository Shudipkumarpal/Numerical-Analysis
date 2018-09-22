import matplotlib.pyplot as plt
import numpy as np

def f(x):
    result = pow(x,10) -10
    return result 

def false_pos (a,b):
    return (b-((f(b)*(a-b))/(f(a)-f(b))))

def error_count (current, previous):
    val = abs((current - previous)/current)*100
    return val

a = 1
b = 2
cnt = 0
              
previous_root_val = 0
Es = 0.5

if (f(a)*f(b)<0):
    while (1):
        cnt = cnt+1
        root_val = false_pos(a,b)
        Ea = error_count (root_val,previous_root_val)
        if(f(a)*f(root_val)==0):
            break
        a = root_val
        if(Ea<=Es):
            break
        previous_root_val = root_val

print("Root Val = ")
print(root_val)
print("Count = ")
print(cnt)

val_x = np.linspace(1,2,num=1000)
plt.plot(val_x,f(val_x) , 'b')
plt.plot(root_val , f(root_val) , 'ro' )
plt.show ()