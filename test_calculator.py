from calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator()
    
    def test_sum(self):
        assert(self.calc.sum(1,2) == 3)