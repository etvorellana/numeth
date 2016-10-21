# -*- coding: utf-8 -*-
# exibe a versão do Python
from platform import python_version
print ("Python "+python_version())

import numeth as nm
import numpy as np
import pylab

coef = [-3.0, -2.0, 1.0, 4.0]

def f(x):
    global coef
    out = nm.polinomio(coef,x)
    return out

def df(x):
    ''' Derivada da função f(x) = x^4 - 15x^2 + 10x +24
     df/dx = f'(x) = 4x^3 - 30x + 10
    '''
    out = 4.0*(x**3.0) - 30.0*x + 10.0
    return out

x = np.arange(-5.0, 5.0, 0.1)
y = nm.polinomio(coef, x)
x_ = np.array(coef)
x_ = -1.0*x_
y_ = nm.polinomio(coef, x_)

pylab.plot(x,y, '-')
pylab.plot(x_,y_, 'o')
pylab.grid(True)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.title("$f(x) = x^4 - 15x^2 + 10x +24$")
#pylab.axis([-5.0, 5.0, -3.0, 15.0])

print ("A função tem 4 Raizes que estão no intervalo (-6,6).")
print ("Vamos procurar os subintervalos de tamanho dx = 0.6." )
subinter = []
N = 0
a = -6.0
b = 6.0
while N < 4:
    x1, x2 = nm.rootsearch(f,a,b,0.6)
    subinter.append((x1,x2))
    a = x2
    N = N + 1

print("Subintervalos onde se encontram as raizes")
print(subinter)

raizesB = []    
for (x1, x2) in subinter:
    p = nm.bisection(f,x1,x2,TOL = 1.0e-9, eType = 0)
    raizesB.append(p)

print("Raizes obtidas pelo método da Bissecção")
print(raizesB)

raizesN = []    
for (x1, x2) in subinter:
    p = nm.newRaph(f,df,x1,TOL = 1.0e-9)
    raizesN.append(p)

print("Raizes obtidas pelo método de Newton-Raphson")
print(raizesN)

raizesNB = []    
for (x1, x2) in subinter:
    p = nm.newRaphBi(f,df,x1,x2,TOL = 1.0e-9)
    raizesNB.append(p)

print("Raizes obtidas pelo método de Newton-Raphson")
print(raizesNB)