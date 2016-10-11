# -*- coding: utf-8 -*-

import numeth as nm
import numpy as np
import pylab

coef = [-3.0, -2.0, 1.0, 4.0]

def f(x):
    global coef
    out = nm.polinomio(coef,x)
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
    x1, x2 = nm.rootsearch(f,a,b,0.6,True)
    subinter.append((x1,x2))
    a = x2
    N = N + 1

raizes = []    
for (x1, x2) in subinter:
    p = nm.bisection(f,x1,x2,TOL = 1.0e-9, eType = 0, pType = True)
    raizes.append(p)


    

