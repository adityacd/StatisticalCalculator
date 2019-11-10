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
    result = 0

    def __init__(self):
        super().__init__()

    def population_mean(self):
        self.result = mean(self.data)
        return self.result

    def population_median(self):
        self.result = median(self.data)
        return self.result

    def population_mode(self):
        self.result = mode(self.data)
        return self.result

    def population_variance(self):
        self.result = variance(self.data)
        return self.result

    def population_standard_deviation(self):
        self.result = standard_deviation(self.data)
        return self.result

    def population_proportion(self):
        self.result = proportion(self.data)
        return self.result

    def population_z_score(self):
        self.result = zscore(self.data)
        return self.result

    def population_confidence_interval(self):
        self.result = confidence_interval(self.data)
        return self.result

    #def population_correlation_coefficient(self):
     #   self.result = population_correlation_coefficient(self.data)
      #  return self.result
