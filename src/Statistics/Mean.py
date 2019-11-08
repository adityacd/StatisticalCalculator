from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(numbers): #complete
    n = len(numbers)
    t = 0
    for x in range(0, n, 1):
        t = float(addition(t, numbers[x]))
    z = float(division(n, t))
    return z