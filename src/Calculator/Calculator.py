from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Subtraction import subtraction
from src.Calculator.Square import square
from src.Calculator.Squareroot import root
from src.Calculator.Multiplication import multiplication


class Calculator:  # Class named 'Calculator'
    result = 0

    def __init__(self):  # Class constructor
        pass

    def add(self, num1, num2):  # Below are the Functions
        self.result = addition(num1, num2)
        return self.result

    def subtract(self, num1, num2):
        self.result = subtraction(num1, num2)
        return self.result

    def multiply(self, num1, num2):
        self.result = multiplication(num1, num2)
        return self.result

    def divide(self, num1, num2):
        self.result = division(num1, num2)
        return self.result

    def square(self, num1):
        self.result = square(num1)
        return self.result

    def square_root(self, num1):
        self.result = root(num1)
        return self.result
