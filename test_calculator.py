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