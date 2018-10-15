import unittest
from solution import MaximumSquare

class TestMaximumSquare(unittest.TestCase):
    def test_01(self):
        strArr = ['10', '01']
        self.assertEqual(1, MaximumSquare(strArr))

    def test_02(self):
        strArr = ["10100", "10111", "11111", "10011"]
        self.assertEqual(4, MaximumSquare(strArr))
    def test_03(self):
        strArr = ["111", "111", "111"]
        self.assertEqual(9, MaximumSquare(strArr))

    def test_04(self):
        strArr = ["110011", "110011", "100001", "111111", "111111", "111111"]
        self.assertEqual(9, MaximumSquare(strArr))


if __name__ == '__main__':
    unittest.main()
