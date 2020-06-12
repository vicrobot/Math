###### S (i^k) , k = 1:n

import numpy as np
from fractions import Fraction
"""
def p(N):
    N += 1

    Y = []

    temp = np.arange(1, N+1)

    Y = (temp**(N-1)).cumsum().reshape(N, -1)

    m_l = [temp]

    for i in range(2,N+1):
        m_l.append(temp**i)

    A = np.asarray(m_l).T

    A = A[:,::-1]

    #print(A)
    #print(Y)
    #print(np.linalg.inv(A).shape, Y.shape)
    X = np.linalg.inv(A)@Y

    #print(X)
    #from fractions import Fraction
    for i in X.ravel():
        print(Fraction(str(i)).limit_denominator(), str(i)[:5], end = ',  ', flush = True)
    print()
    print('-'*50)

for count in range(20):
    p(count)
"""

from sympy.matrices import Matrix

def p(N):
    N += 1

    Y = []

    temp = np.arange(1, N+1)

    Y = (temp**(N-1)).cumsum().reshape(N, -1)

    m_l = [temp]

    for i in range(2,N+1):
        m_l.append(temp**i)

    A = np.asarray(m_l).T

    A = A[:,::-1]

    #print(A)
    #print(Y)
    #print(np.linalg.inv(A).shape, Y.shape)
    A = Matrix(A)
    Y = Matrix(Y)
    
    X = (A**-1)*Y
    print(X)

    #print(X)
    #from fractions import Fraction
    #for i in X.ravel():
    #    print(Fraction(str(i)).limit_denominator(), str(i)[:5], end = ',  ', flush = True)
    #print()
    #print('-'*50)

for count in range(15):
    p(count)







