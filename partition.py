import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from sympy import factorial

def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def g(n,k):
    ps = list(partitions(n))
    return len([i for i in ps if len(i) == k])

def starsbars(n,k):
    # (n-1)C(k-1)
    return comb(n-1, k-1)

def stirlings(n,k):
    fact_a_1 = factorial(k)
    fact_a_2 = 0
    for i in range(k+1):
        fact_b_1 = (-1)**i
        fact_b_2 = comb(k,i)
        fact_b_3 = (k-i)**n
        fact_a_2 += fact_b_1* fact_b_2* fact_b_3
    return fact_a_1*fact_a_2

N,K = 50, 50

array = []

for n in range(1,N+1):
    for k in range(1, K+1):
        array.append( (int(g(n,k)), int(stirlings(n,k)), int(starsbars(n,k))) )
        

sarray = set(array)
lmatrix = [list(i) for i in array]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Example data: replace this with your actual data
data = np.array(lmatrix)

# Extract x, y, z coordinates
z = data[:, 0] #partitions (n,k)
x = data[:, 1] #stirling numbers (n,k)
y = data[:, 2] #starsbars (n,k) theorem 1

# Create a new figure
fig = plt.figure()

# Add 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot data
ax.scatter(x, y, z)

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
plt.show()





















    
