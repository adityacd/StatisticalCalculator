import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CSVReading.CSVReading import CsvReader
from pprint import pprint
import statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statobj = Statistics('Data/StatData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statobj, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statobj, Statistics)

    def test_Population_Mean_calculator(self):  #complete
        print(' ')
        print('Testing Population Mean')
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            a = int(row['Value 1'])
            dataset.append(a)
        for column in answer:
            result = float((column['Mean']))
        self.assertEqual(self.statobj.population_mean(dataset), result)

    def test_Median_calculator(self):  #complete
        print(' ')
        print('Testing Population Median')
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Median']))
        self.assertEqual(self.statobj.population_median(dataset), result)

    def test_Mode_calculator(self):  #complete
        print(' ')
        print('Testing Population Mode')
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Mode']))
        self.assertEqual(self.statobj.population_mode(dataset), result)

    def test_Population_Standard_Deviation_calculator(self):  #complete
        print(' ')
        print('Testing Population Standard Deviation')
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['StanDeviation']))
        self.assertEqual(self.statobj.population_standard_deviation(dataset), result)

    def test_Population_Variance_calculator(self):   #complete
        print(' ')
        print('Testing Population Variance')
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['Variance']))
        self.assertEqual(self.statobj.population_variance(dataset), result)

    def test_Sample_Standard_Deviation_calculator(self):  #complete
        print(' ')
        print('Testing Sample Standard Deviation')
        test_data = CsvReader('Data/StatData.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        x, z = self.statobj.sampstdev(dataset)
        x = round(x, 3)
        z = round(z, 3)
        self.assertEqual(x, z)

    def test_Sample_Mean_calculator(self):
        print(' ')
        print('Testing Sample Mean')
        test_data = CsvReader('Data/StatData.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        x, z = self.statobj.samplemean(dataset)
        #z = self.statobj.samplemean(dataset)
        self.assertEqual(x, z)

    """
    def test_z_score_calculator(self):
        print('Testing ZScore')
        test_data = CsvReader('Data/StatData.csv').data
        for row in test_data:
            y = int(row['Value 1'])
            result = float(row['Result'])
            self.assertEqual(self.statobj.z_score(y), result)
"""
"""
    def test_proportion_calculator(self):
        test_data = CsvReader('Data/StatData.csv').data
        answer = CsvReader('Data/StatDataAnswers.csv').data
        dataset = []
        for row in test_data:
            y = int(row['Value 1'])
            dataset.append(y)
        for column in answer:
            result = float((column['proportion']))
        self.assertEqual(self.statobj.proportion(dataset), result)
"""

