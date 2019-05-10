
'''
roots.py



Adapted from the book Numerical Methods for
Chemical Engineers with MATLAB Applications
by Constantinides & Mostoufi

'''

class Roots():

    def __init__(self,func,x0,tol=1e-6,trace=0,itermax = 100):
        self.x0 = x0
        self.func = func
        if tol == 0:
            self.til = 1e-6
        else:
            self.tol = tol
        self.trace = trace

    def plot()
