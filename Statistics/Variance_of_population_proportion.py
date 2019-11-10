from Statistics.Proportion import proportion
from Statistics.Variance import variance


def variance_of_population_proportion(numbers):
    variance_value = proportion(numbers)
    return variance(variance_value)
