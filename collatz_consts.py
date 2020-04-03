#import pandas as pd

dict_nums = {}


def collatz(num):
    d_x = {'n':0,'ts':[]}
    if(num%2==0):
        num1 = num
        k = 0
        while(num1%2==0):
            k+=1
            num1 = num1/2
        d_x['ts'].append(k)
        num = num1
    n = 0
    num1 = num
    while num1 !=1:
        t = 0
        num2 = 3*num1+1
        while (num2%2==0):
            t+=1
            num2 = num2/2
        d_x['ts'].append(t)
        num1 = num2
        n += 1
    d_x['n'] += n
    return d_x

def f(a, x, d):
    ts = d['ts']
    n = d['n']
    if x%2 == 0:
        a = a/(2**ts[0])
        if(len(ts) == 1): return a
        else:  ts = ts[1:]
    for i in range(n):
        a = (3*a + 1)/2**(ts[i]) #and thus n = len(ts) if x%2 else len(ts)-1
    return a
    
    
    
init, end = 2, 5000
for i in range(init, end):
    dict_nums[i] = collatz(i)

#df = pd.DataFrame(dict_nums.values())
#print(dict_nums)
#print(df)
#print('-'*20)

consts = []
for x,d in dict_nums.items():
    a = 2
    temp = f(a*x,x,d)
    consts.append((temp - a)/(1-a))

m = max(consts)
print(m, consts.count(m), consts.index(m), len(consts) )
#print(dict_nums[993])


import numpy as np
import matplotlib.pyplot as plt
#fig, (ax1, ax2) = plt.subplots(1,2)
#from matplotlib import style
#style.use('dark_background')
plt.grid('True')
x = np.arange(init+1, end, 2)
y = consts[1::2]
x1 = np.arange(init, end,2)
y1 = consts[::2]
plt.scatter(x, y)
plt.scatter(x1, y1)
plt.legend(['odds', 'evens'])
plt.show()







































