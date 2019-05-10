class Polynomial():
from .derivative import Derivative

    def __init__(self, coef=[0]):
        self.coef = np.array(coef)
        self.exp = self._determine_exponents(self.coef)
        pass

    def _determine_exponents(self):
        # Create list of exponents based on size of array
        return list(range(len(self.coef),-1,-1))

    def result(self,x):
        # calculates y for the polynomail funciton given x
        return np.power(np.array(self.coef)*x,self.exp).sum()

    def make_derivative(self):
        Derivative(list(self.coef))
        pass

    def make_integral(self):
        pass

    def __repr__(self):
        rep_str = "Polynomial Order: {}.format()"
        pass
