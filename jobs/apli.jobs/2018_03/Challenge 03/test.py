import unittest
from solution import liquid_distribution

class TestLiquidDistribution(unittest.TestCase):
    def test_01(self):
        liters = 18
        bottles = [1, 2, 5, 10]
        self.assertEqual(4, liquid_distribution(liters, bottles))

    def test_02(self):
        liters = 9
        bottles = [1, 4, 6]
        self.assertEqual(3, liquid_distribution(liters, bottles))

    def test_03(self):
        liters = 4
        bottles = [1, 2, 3]
        self.assertEqual(2, liquid_distribution(liters, bottles))

    def test_04(self):
        liters = 37
        bottles = [0, 3, 17, 36, 57, 81, 92]
        self.assertEqual(3, liquid_distribution(liters, bottles))

    def test_05(self):
        liters = 0
        bottles = [1, 2, 3, 4, 5]
        self.assertEqual(0, liquid_distribution(liters, bottles))

    def test_06(self):
        liters = 9
        bottles = [2, 4, 6]
        self.assertEqual(-1, liquid_distribution(liters, bottles))


if __name__ == '__main__':
    unittest.main()
