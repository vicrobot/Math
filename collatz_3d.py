#!/bin/env python3

##### THEORY ######

""""
Axis details-
x - 2**n (0,1,2,...)
y - 3**n (0,1,2,...)
z - num (1,2,3,...)

Example for coord collection for x,y:-
3 -> (1 = t0) -> 5 -> (4 = t1) -> 1

So - sum(tis) = 1+4 = 5.
2**sum(tis) = 32

32*1 = 3*(3**(n=2)) + (2**0)*(3**(n=2-1=1)) + ((2**t0=1)*(3**(n=1-1=0))
Thus, we see- 

For num 3-
we have a pair seq of powers of 2 and 3 after a*3**n as - (0,1),(1,0)

For 5 we will have (1,0)

Similarly we'll get 3d coords for num as-

(0,n-1,num),(t0,n-2,num),(t0+t1,n-3,num),(t0+t1+t2,n-4,num),....(t0+...+t(n-2), 0,num)

where n is its cycle length.
"""


################ IMPORTS ##########################

from collatz_consts import collatz
import pdb
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from math import log

###################################################
###################################################

def getCoords(num,coords_3d=True,give_n=False):
    # breakpoint()
    n, tis = collatz(num).values()
    print(f'For {num=}, received {n=},{tis=}')
    # have first elem as 0, which somehow is strange agraj of tis
    p=log(num,2)
    #coords = [(p,n,num) if coords_3d else (p,n)]
    coords = []
    coords.append((0,n-1,num) if coords_3d else (0,n-1))
    counter_3_power = n-2
    # loop over t0 to t(n-2)
    for ti in tis[:-1]:
        sum_till_t_i = coords[-1][0] + ti
        if coords_3d:
            coords.append( (sum_till_t_i, counter_3_power,num) ) # (x=2**i,y=3**i,z=num)
        else:
            coords.append( (sum_till_t_i, counter_3_power) ) # (x=2**i,y=3**i)
        counter_3_power -= 1
    if give_n:
        return coords,n
    else:
        return coords

def plotter2d():
    #style.use('dark_background')
    fig,ax=plt.subplots()
    legend = []
    ax.grid('True')
    ax.set_title(r'$unmukti$')
    ax.set_xlabel(r'$x=2^i$')
    ax.set_ylabel(r'$x=3^i$')
    global llim,ulim
    for num in range(llim,ulim+1,2):
        coords = getCoords(num,coords_3d=False)
        x=[x for x,y in coords]
        y=[y for x,y in coords]
        ax.plot(x,y)
        #legend.append(repr(num))
        for i_x, i_y in zip(x, y):
            #ax.text(i_x, i_y, '{}'.format(num))
            break
    #ax.legend(legend)
    plt.show()

def plotter3d():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title(r'$unmukti$')
    ax.set_xlabel(r'$x=2^i$')
    ax.set_ylabel(r'$x=3^i$')
    ax.set_zlabel(r'num')
    global llim,ulim
    for num in range(llim,ulim+1,2):#list(range(100,156,2) )+list( range(1000,1050,2)):
        coords,n = getCoords(num,coords_3d=True,give_n=True)
        x=np.asarray([x for x,y,z in coords])
        y=np.asarray([y for x,y,z in coords])
        z=[z for x,y,z in coords]
        #breakpoint()
        z=np.asarray(z)
        ax.plot(x,y,z)
        #legend.append(repr(num))
        for i_x, i_y,i_z in zip(x,y,z):
            #ax.text(i_x, i_y,i_z, '{}'.format(num))
            break
    #ax.legend(legend)
    plt.show()

############ RUN POINT ################
if __name__ == '__main__':
    #print(getCoords(27))
    llim,ulim=101,151
    plotter3d()




# 143- n = 37
# [1, 1, 1, 4, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 4, 3, 1, 1, 5, 4]


# 47- n = 38
# [1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 4, 3, 1, 1, 5, 4]




















