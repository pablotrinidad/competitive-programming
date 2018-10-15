import unittest
from solution import divisible_by_5

class TestTimeConversion(unittest.TestCase):
    def test_01(self):
        self.assertEqual('1010', divisible_by_5('0100,0011,1010,1001'))

    def test_02(self):
        self.assertEqual('101,11001', divisible_by_5('101,1110,11111,1,11001'))

    def test_03(self):
        self.assertEqual('11110,1010', divisible_by_5('011,11110,1010'))


if __name__ == '__main__':
    unittest.main()
