import numpy as np

class Calculator:
    def sum(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

    def sqrt(self, n):
        if (n < 0):
            raise ArithmeticError
        return np.sqrt(n)