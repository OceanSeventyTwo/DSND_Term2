import numpy as np
from .polynomial import Polynomial

class Derivative(Polynomial):

    def __init__(self, coef=[0]):
        Polynomial.__init__(self,coef)
        self.exp = self._determine_exponents(self.coef)
        self.derivate()

    def derivate(self):
        self.coef = np.multiply(self.coef,self.exp)[:-1]
        self.exp = self.exp[:-1]-1
