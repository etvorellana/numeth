# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:54:22 2016

@author: evalero
"""

import numeth as nm
import numpy as np
import math as mt
import pylab


# Polinômio de Taylor para f(x)= cos(x) em torno de X_0 = 0
#f(x) = cos(x)           f(x_0)= 1.0
#f'(x) = -sen(x)         f'(x_0)= 0.0
#f''(x) = -cos(x)        f''(x_0)= -1.0
#f'''(x) = sen(x)        f'''(x_0)= 0.0
#f''''(x) = cos(x)       f''''(x_0) = 1.0

# Polinômio da Taylor de grau 3

def fatorial(x):
    if x == 0:
        return 1
    out = x
    x = x -1
    while x > 0:
        out = out * x
        x = x - 1;
    return out

def p_n(n,x):
    out = 0
    sinal = 1.0;
    for k in range(0,n+1,2):
        out = out + (sinal/fatorial(k))*(x**k)
        sinal *= -1.0
    
    return out
        
x = np.arange(-2.0, 2.1, 0.1)
y = np.arange(-2.0, 2.1, 0.1)
y_ = np.arange(-2.0, 2.1, 0.1)
y__ = np.arange(-2.0, 2.1, 0.1)
y___ = np.arange(-2.0, 2.1, 0.1)
for i in range(len(y)):
    y[i] = mt.cos(x[i])
    y_[i] = p_n(2,x[i])
    y__[i] = p_n(4,x[i])
    y___[i] = p_n(6,x[i])
    

pylab.plot(x,y, '-', label="$\cos(x)$")
pylab.plot(x,y_, '--', label="$p_2(x)$")
pylab.plot(x,y__, '-.', label="$p_4(x)$")
pylab.plot(x,y___, '.', label="$p_6(x)$")
pylab.grid(True)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.title("$f(x) = \cos (x)$")
pylab.axis([-2.1, 2.1, -0.6, 1.2])
pylab.legend()



        
    