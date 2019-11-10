from Statistics.Mean import population_mean
from Statistics.StandardDeviation import population_standard_deviation
from Calculator.Squareroot import square_root


def confidence_interval(numbers):
    x1 = population_mean(numbers)
    c = 0.95
    z_value = (1-c) / 2
    d1 = population_standard_deviation(numbers)
    l1 = square_root(len(numbers))
    return [x1 - z_value*d1 / l1, x1 + z_value*d1 / l1]