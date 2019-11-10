import random


def sample_method(numbers):
    r = random.randint(30, 51)
    sample_list = random.sample(numbers, r)
    return sample_list