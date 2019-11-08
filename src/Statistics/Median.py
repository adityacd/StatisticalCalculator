from src.Calculator.Addition import addition
from src.Calculator.Division import division


def median(numbers):  # complete
    numbers.sort()
    print(numbers)
    n = len(numbers)
    if n % 2 == 0:
        x = division(2, addition(division(2, addition(n, 2)), division(2, n)))
        return print('Median is ', x)
    else:
        x = int(division(2, addition(n, 1)))
        return print('Median is ', numbers[x - 1])
