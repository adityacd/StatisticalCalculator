from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
from Calculator.Squareroot import root


def confidence_interval(numbers):
    x1 = mean(numbers)
    c = 0.95
    z_value = (1-c) / 2
    d1 = standard_deviation(numbers)
    l1 = root(len(numbers))
    return [x1 - z_value*d1 / l1, x1 + z_value*d1 / l1]