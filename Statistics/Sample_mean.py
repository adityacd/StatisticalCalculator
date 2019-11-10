from Statistics.Sample_method import sample_method
from Statistics.Mean import mean


def sample_mean(numbers):
    sample_list1 = sample_method(numbers)
    return mean(sample_list1)
