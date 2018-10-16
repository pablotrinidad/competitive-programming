import unittest
from solution import maximum_square

class TestMaximumSquare(unittest.TestCase):
    def test_01(self):
        strArr = ['10', '01']
        self.assertEqual(1, maximum_square(strArr))

    def test_02(self):
        strArr = ["10100", "10111", "11111", "10011"]
        self.assertEqual(4, maximum_square(strArr))
    def test_03(self):
        strArr = ["111", "111", "111"]
        self.assertEqual(9, maximum_square(strArr))

    def test_04(self):
        strArr = ["110011", "110011", "100001", "111111", "111111", "111111"]
        self.assertEqual(9, maximum_square(strArr))


if __name__ == '__main__':
    unittest.main()
