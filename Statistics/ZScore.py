from Calculator.Division import division
from Calculator.Subtraction import subtraction

from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation

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