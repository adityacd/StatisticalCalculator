from src.Calculator.Division import division
from src.Calculator.Subtraction import subtraction

from src.Statistics.Mean import mean
from src.Statistics.StandardDeviation import standard_deviation

def zscore(numbers): #complete
    u = mean(numbers)
    sig = standard_deviation(numbers)
    n = len(numbers)
    zsc = []
    for i in range(0, n, 1):
        z = 0
        z = float(division(sig, subtraction(u, numbers[i])))
        #z = float((numbers[i] - u) / sig)
        zsc.append(z)
    return print('Zscore is', zsc)