import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CSVReading.CSVReading import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Data/StatData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Population_Mean_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            a = int(row['Value 1'])
            dataset.append(a)
        for column in answer:
            result = float((column['Mean']))
        self.assertEqual(self.statistics.population_mean(dataset), result)

    def test_Median_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Median']))
        self.assertEqual(self.statistics.population_median(dataset), result)

    def test_Mode_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Mode']))
        self.assertEqual(self.statistics.population_mode(dataset), result)

    def test_Population_Standard_Deviation_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['StanDeviation']))
        self.assertEqual(self.statistics.population_standard_deviation(dataset), result)

    def test_Population_Variance_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Variance']))
        self.assertEqual(self.statistics.population_variance(dataset), result)
