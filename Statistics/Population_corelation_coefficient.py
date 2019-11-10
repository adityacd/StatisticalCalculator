from Statistics.ZScore import zscore


def population_correlation_coefficient(numbers, numbers1):
    z1 = zscore(numbers)
    z2 = zscore(numbers1)
    z1_z2 = list(map(lambda x, y: x * y, z1, z2))
    p = sum(z1_z2) / len(z1_z2)
    return p
