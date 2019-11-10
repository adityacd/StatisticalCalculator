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
