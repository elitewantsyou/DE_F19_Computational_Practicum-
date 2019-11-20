from . import Controller
from . import View
from sympy import symbols, exp

class Model():
    def __init__(self, root, x0=0, y0=(0.5)**(0.5), X=3, n=100):
        x, y, c1 = symbols("x y c1")
        self.function = exp(x ** 2 / 2)/ ((c1 + exp(x ** 2))**0.5)
        self.function_dash = x*y-x*y**3
        # print(self.function)
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.n = n
        self.controller = Controller.Controller(self.function_dash, self.function, x0, y0, X, n)
        self.view = View.View(root, self.controller)
    
        