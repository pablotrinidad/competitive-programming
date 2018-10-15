import unittest
from solution import kaprekars_constant

class TestKaprekarsConstant(unittest.TestCase):
    def test_01(self):
        num = 6174
        self.assertEqual(1, kaprekars_constant(num))

    def test_02(self):
        num = 2111
        self.assertEqual(5, kaprekars_constant(num))

    def test_03(self):
        num = 9831
        self.assertEqual(7, kaprekars_constant(num))

    def test_04(self):
        num = 3524
        self.assertEqual(3, kaprekars_constant(num))

    def test_05(self):
        num = 9237
        self.assertEqual(3, kaprekars_constant(num))


if __name__ == '__main__':
    unittest.main()
