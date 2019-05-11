import numpy as np
from .polynomial import Polynomial

class Derivative(Polynomial):

    def __init__(self, coef=[0],order=1):
        Polynomial.__init__(self,coef)
        self.dcoef = self.coef
        self.dexp = self._determine_exponents()
        self.order = order
        if order > self.exp[0]:
            print('Warning: Order larger than the polynomial')
        self.derivate(order)

    def derivate(self,order):
        for i in range(1,order+1):
            self.dcoef = np.multiply(self.dcoef,self.dexp)[:-1]
            self.dexp = self.dexp[:-1]-1
    
    def __repr__(self):
        rep_str = "Polynomial: "
        der_str = "Order " + str(self.order) + " Derivative: "
        for i in range(len(self.coef)):
            if self.exp[i] > 0:
                rep_str += str(self.coef[i])+'x^'+str(self.exp[i])+ ' + '
            else:
                rep_str += str(self.coef[i])
        for i in range(len(self.dcoef)):
            if self.dexp[i] > 0:
                der_str += str(self.dcoef[i])+'x^'+str(self.dexp[i])+ ' + '
            else:
                der_str += str(self.dcoef[i])
        return rep_str +' \n' + der_str
