# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:05:57 2016

@author: evalero
"""

import numpy as np
import math as mt

def bisection(f,a,b,TOL = 1.0e-9, eType = 0, pType = False):
    ''' root = bisection(f,a,b,TOL=1.0e-9,eType=0,pType=False).
    Procura a raiz f(x) = 0 pelo método da bissecção.
    A Raiz deve estar contida no ontervalo (a,b). 
    Para pType = True a execução das iterações são detelhadas
    '''
    N_0 = int(mt.ceil(mt.log(abs(b - a)/TOL)/mt.log(2.0)))
    if(pType == True):
        print("N_0 = %d" % (N_0))
    #Passo 1
    i = 1
    FA = f(a)
    #Passo 2
    if(pType == True):
        print("i \ta_i \t\tb_i \t\tp_i \t\tf(p_i) \t\tepsilon")
    Ok = False
    p_n = a
    while i <= N_0:
        #Passo 3
        p = a + (b - a)/2 
        FP = f(p)
        if (eType == 0):
            error = (b - a)/2
        elif (eType == 1):
            error = abs(p - p_n)
        elif (eType == 2):
            error = abs(p - p_n)/abs(p)
        else:
            error = abs(FP)
        if(pType == True):    
            print("%d\t%f\t%f\t%f\t%f\t%f" % (i, a, b, p, FP, error))
        #Passo 4
        if FP == 0.0 or error < TOL:
            return p
        #Passo 5
        i = i + 1
        #Passo 6
        if np.sign(FA) == np.sign(FP) :
            a = p
            FA = FP
        else:
            b = p
        p_n = p

def newRaph(f, df, p, TOL = 1.0e-9, N_0 = 30):
    #Passo 1
    for i in range(N_0):
        #Passo 2
        fp = f(p)
        dfp = df(p)
        try:
            dp = -fp/dfp
        except ZeroDivisionError: 
            print("df(p) = 0")
            return none
        
        #Passo 3
        p = p + dp
        #Passo 4
        if abs(dp) < TOL:
            return p
    
    #Passo 5
    print("O método falhou após %d iterações" % (N_0))
    return none
    
def newRaphBi(f, df, a, b, TOL = 1.0e-9):
    #Passo 1
    N_0 = int(mt.ceil(mt.log(abs(b - a)/TOL)/mt.log(2.0)))
    #Passo 2
    fa = f(a)
    if fa == 0.0:
        return a
    fb = f(b)
    if fb == 0.0:
        return b
    if np.sign(fa) == np.sign(fb):
        print("O intervalo pode não conter raizes")
        return None
    #passo 3
    p = a + (b - a)/2
    #passo 4
    for i in range(N_0):
        #Passo 5
        fp = f(p)
        dfp = df(p)
        try:
            dp = -fp/dfp
        except ZeroDivisionError:
            if np.sign(fa) == np.sign(fp) :
                a = p
                fa = fp
            else:
                b = p
                fb = fp
            dp = (b-a)/2
        #Passo 3
        p = p + dp
        #Passo 4
        if abs(dp) < TOL:
            return p
    
    #Passo 5
    print("O método falhou após %d iterações" % (N_0))
    return none


def rootsearch(f,a,b,dx,pType = False):
    ''' x1,x2 = rootsearch(f,a,b,dx,pType = False).
    Procura no intervalo (a,b), com incrementos dx, por
    um subintervalo (x1,x2) onde possa ser encontrada 
    uma raiz para f(x). Basicamente, procura um subintervalo
    (x1,x2), de tamanho dx, para o qual f(x1)*f(x2) < 0.
    Retorna x1 = x2 = None se não achar subintervalo 
    apropriado.
    Para pType = True a execução das iterações são detelhadas   
    '''
    if pType:
        print('Procurando no intervalo (%f,%f) ' % (a,b))
        print('com incremendo dx = %f' % (dx))
    x1 = a 
    f1 = f(a)
    if pType:
        print ("x1 = %f, f(x1) = %f" % (x1,f1))
    x2 = a + dx
    f2 = f(x2)
    while np.sign(f1) == np.sign(f2):
        if pType:
            print ("x2 = %f, f(x2) = %f" % (x2,f2))
        if x1  >=  b: return None,None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        if pType:
            print ("x2 = %f, f(x2) = %f" % (x2,f2))
        return x1,x2
        
def polinomio(coef, x):
    ''' y = polinomio(coef,x)
    Retorna o polinomio p(x)=(x+x_0)(x+x_1)...(x+x_{N-1})
    onde x_i, para i = 0...N-1, são os elementos da lista
    coef de tamanho N. Tratase de um polinômio de grau N
    '''
    N = len(coef)
    out = 1.0
    while N > 0:
        out = out * (x + coef[N-1])
        N = N - 1
    return out

