from CSVReading.CSVReading import CsvReader
from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Proportion import proportion
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.Population_corelation_coefficient import population_correlation_coefficient
from Statistics.Confidence_interval import confidence_interval
from Statistics.ZScore import zscore


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Data/StatData.csv').data
        super().__init__()

    def population_mean(self, a):
        self.result = mean(a)
        return self.result

    def population_median(self, a):
        self.result = median(a)
        return self.result

    def population_mode(self, a):
        self.result = mode(a)
        return self.result

    def population_variance(self, a):
        self.result = variance(a)
        return self.result

    def population_standard_deviation(self, a):
        self.result = standard_deviation(a)
        return self.result

    def population_proportion(self, a):
        self.result = proportion(a)
        return self.result

    def population_z_score(self, a):
        self.result = zscore(a)
        return self.result

    def population_confidence_interval(self, a):
        self.result = confidence_interval(a)
        return self.result

    # def population_correlation_coefficient(self):
    #   self.result = population_correlation_coefficient(self.data)
    #  return self.result
