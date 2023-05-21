import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,4, 1) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self,5, 1) == 4

    def test_division(self):
        assert self.calc.division(self,15, 5) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 2) == 10

    def teardown(self):
        print('Выполнение метода Teardown')