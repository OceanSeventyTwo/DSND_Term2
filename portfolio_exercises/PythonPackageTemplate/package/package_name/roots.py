'''
roots.py

Inherits Polynomial and Derivative Classes

Adapted from the book Numerical Methods for
Chemical Engineers with MATLAB Applications
by Constantinides & Mostoufi

Uses three methods to find the roots of a polynomial equation.


'''

from .polynomial import Polynomial
from .derivative import Derivative

class Roots(Polynomial,Derivative):

    def __init__(self,coef=[],x0,tol=1e-6,trace=0,itermax = 100,method='NR'):
        
        Polynomial.__init__(self,coef)
        Derivative.__init__(self,coef)
        
        self.x0 = x0
        self.func = func
        if tol == 0:
            self.til = 1e-6
        else:
            self.tol = tol
        self.trace = trace
        self.method = method

    def plot()
