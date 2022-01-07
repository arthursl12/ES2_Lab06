from calculator import Calculator
import pytest
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
        