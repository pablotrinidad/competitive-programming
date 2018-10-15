import unittest
from solution import sum_chars

class TestTimeConversion(unittest.TestCase):
    def test_01(self):
        self.assertEqual(38, sum_chars('Apli'))

    def test_02(self):
        self.assertEqual(431, sum_chars('Donaudampfschifffahrtsgesellschaftskapitaen'))

    def test_03(self):
        self.assertEqual(54, sum_chars('Campeche'))

    def test_04(self):
        self.assertEqual(108, sum_chars('TheXFiles'))


if __name__ == '__main__':
    unittest.main()

