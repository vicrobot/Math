from math import sqrt
from numpy import isclose
import re


"""
The
    relative difference (`rtol` * abs(`b`)) and the absolute difference
    `atol` are added together to compare against the absolute difference
    between `a` and `b`

(a-b)**3 = a**3 - b**3 - 3*a*b*(a - b)
"""

fx = '3*x**7 + 48*x**2 - 2*x**1 +34*x**0 -2*x**10 + 123*x**0'  # the format a*x**b is necessary.

digger = re.compile('[-+]*[0-9.]+\*x\*\*[0-9.]+')


def coeffnexpo(string):
    main1 = string.split('*')
    coeff = float(main1[0])
    expo = float(main1[-1])
    return coeff, expo

def modified(num):
    if num < 0: return '{}'.format(num)
    else: return '+{}'.format(num)

def composer(tup_list):
    head = 'lambda x: '
    tail = ' '.join(['{}*x**{}'.format(modified(i),j) for i, j in tup_list])
    k1 = head + tail
    return tail, eval(k1)

def parser(str_func):
    return eval('lambda x: ' + str_func)

def derivative(str_func):
    last_return = '0*x**0'
    if not str_func.strip(): return last_return
    main_list = digger.findall(str_func)
    tup_list = list(map(coeffnexpo, main_list))
    if tup_list[0][0] == 0: return last_return
    else:
        der_list = []
        for i,j in tup_list:
            if j == 0: continue
            else:
                der_list.append((i*j, j-1))
    if not der_list: return last_return
    return composer(der_list)


"""
fx = lambda x: 90*x**7 +1*x**6 -4*x**4 - 3*x**3 + 4*x**2 - 2*x**1 +34*x**0  #writing x**1 instead of x for re easiness.
f1x = lambda x: 630*x**6 +6*x**5 -16*x**3 - 9*x**2 + 8*x**1 - 2*x**0
f2x = lambda x: 3780*x**5 +30*x**4 -48*x**2 - 18*x**1 + 8*x**0

# some sets for examples
fx = lambda x: 3*(x**3) + 4*(x**2) - 2*x +34
f1x = lambda x: 9*(x**2) + 8*x - 2
f2x = lambda x: 18*x + 8

fx = lambda x: (x**3) - 9*(x**2) - 27*x -27
f1x = lambda x: 3*(x**2) - 18*x - 27
f2x = lambda x: 6*x  -18

fx = lambda x: x**7 -1*x**6 -4*x**4 + 3*(x**3) + 4*(x**2) - 2*x +34
f1x = lambda x: 7*x**6 -6*x**5 -16*x**3 + 9*(x**2) + 8*x - 2
f2x = lambda x: 42*x**5 -30*x**4 -48*x**2 + 18*x + 8
"""

def do_iter(fx, f1x, f2x, a):
    """
    Returns the root of 2nd degree taylor polynomial  expectation of fx calculated on x = a
    """
    a_coeff = f2x(a)
    b_coeff = 2*(f1x(a) - a*f2x(a))
    c_coeff = 2*fx(a) + (a**2)*f2x(a) - 2*a*f1x(a)
    part2 = sqrt(abs( b_coeff**2 - 4*a_coeff*c_coeff )) # this will cause error because of abs, and abs is wrong
                                                        # since the root was complex if error is there.
                                                        # but main problem is that, it is somehow giving right
                                                        # answer even when abs is there.
    
    num1 = -b_coeff + part2
    num2 = -b_coeff - part2
    denm = 2*a_coeff
    x1 = num1/denm
    x2 = num2/denm
    return x1 if abs(fx(x1)) < abs(fx(x2)) else x2

def do_iter_1deg(fx, f1x, f2x, a):
    x  = a - (fx(a)/f1x(a))
    return x

class detect:
    def __init__(self, fx):
        """ fx is the polynomial function. 
            All terms are expected in the form a*x**b
        Ex: -48*x**2 - 18*x**1 + 8*x**0
        """
        self.fx_s, self.fx = fx, parser(fx)
    def derivative(self, gx):
        """ returns polynomial string of derivative and derivative function 
        Ex:
        >>> print(detect('-48*x**2 - 18*x**1 + 8*x**0').derivative('-48*x**2 - 18*x**1 + 8*x**0'))
        ('-96.0*x**1.0 +18.0*x**0.0', <function <lambda> at 0x7faf0436c7b8>)
        """
        #has to return derivative of gx i.e. g1x
        return derivative(gx)
    def root(self, typ = 'newraphtay'):
        """
        returns a root of fx.
        typ::= 'newraphtay': 
                    uses special algorithm merge of taylor series with newton-raphson
               'newraph': 
                    uses classic newton-raphson method
        Ex:
        >>> fx = '-48*x**2 - 18*x**1 + 8*x**0'
        >>> print(detect(fx).root())
        -0.636747208370073
        """
        if typ != 'newraphtay' and typ!= 'newraph':
            raise ValueError('Wrong argument for "typ"\n')
        f1x_s, f1x = self.derivative(self.fx_s)
        f2x_s, f2x = self.derivative(f1x_s)
        fx = self.fx
        a, counter = 10, 0
        while not isclose(0, fx(a), rtol = 1e-5, atol = 1e-5):
            counter += 1
            if counter > 2000:
                print('Many iterations')
                break
            if typ == 'newraphtay': a = do_iter(fx, f1x, f2x, a)
            elif typ == 'newraph': a = do_iter_1deg(fx, f1x, f2x, a)
        #print(a, '{} Iterations: {}'.format(typ, counter), fx(a))
        return a, counter

method1, method2 = 'newraphtay','newraph'
root_val, iterations = detect(fx).root(typ = method1)
print('method: {}, iterations: {}'.format(method1, iterations))
print('Value of function on {}:'.format(root_val), eval('lambda x: '+ fx)(root_val))
root_val, iterations = detect(fx).root(typ = method2)
print('\nmethod: {}, iterations: {}'.format(method2, iterations))
print('Value of function on {}:'.format(root_val), eval('lambda x: '+ fx)(root_val))

# old version of this file; not including upper defs
"""
def root(fx, f1x, f2x, typ = 'newraphtay'):
    a, counter = 10, 0
    while not isclose(0, fx(a), rtol = 1e-5, atol = 1e-5):
        counter += 1
        if counter > 2000:
            print('Many iterations')
            break
        if typ == 'newraphtay': a = do_iter(fx, f1x, f2x, a)
        elif typ == 'newraph': a = do_iter_1deg(fx, f1x, f2x, a)
    print(a, '{} counts: {}'.format(typ, counter), fx(a))
    return a

fx = lambda x: x**7 -1*x**6 -4*x**4 + 3*(x**3) + 4*(x**2) - 2*x +34
f1x = lambda x: 7*x**6 -6*x**5 -16*x**3 + 9*(x**2) + 8*x - 2
f2x = lambda x: 42*x**5 -30*x**4 -48*x**2 + 18*x + 8

root(fx, f1x, f2x, typ = 'newraph')
root(fx, f1x, f2x, typ = 'newraphtay')
"""

