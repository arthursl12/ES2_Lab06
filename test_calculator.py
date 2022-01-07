import pytest

from calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator()
    
    def test_sum(self):
        assert(self.calc.sum(1,2) == 3)
    
    def test_subtraction(self):
        assert(self.calc.subtraction(10,3) == 7)
    
    def test_subtraction_negative_result(self):
        assert(self.calc.subtraction(2,6) == -4)
    
    def test_multiplication(self):
        assert(self.calc.mult(15,14) == 210)
        
    def test_division(self):
        assert(self.calc.div(100,5) == 20)
    
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10,0)
    
    def test_square_root(self):
        assert(self.calc.sqrt(4) == 2)
        assert(pytest.approx(self.calc.sqrt(2), 0.01) == 1.41)
        
    def test_square_root_of_negative(self):
        with pytest.raises(ArithmeticError):
            self.calc.sqrt(-10)
    
    def test_exponential(self):
        assert(self.calc.exp(5,4) == 625)
    
    def test_exponential_negative_exponent(self):
        assert(pytest.approx(self.calc.exp(4,-3), 1e-6) == 0.015625)
        
        