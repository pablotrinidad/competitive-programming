import unittest
from solution import KaprekarsConstant

class TestKaprekarsConstant(unittest.TestCase):
    def test_01(self):
        num = 6174
        self.assertEqual(1, KaprekarsConstant(num))

    def test_02(self):
        num = 2111
        self.assertEqual(5, KaprekarsConstant(num))

    def test_03(self):
        num = 9831
        self.assertEqual(7, KaprekarsConstant(num))

    def test_04(self):
        num = 3524
        self.assertEqual(3, KaprekarsConstant(num))

    def test_05(self):
        num = 9237
        self.assertEqual(3, KaprekarsConstant(num))


if __name__ == '__main__':
    unittest.main()
