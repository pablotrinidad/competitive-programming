import unittest
from solution import heads_and_legs

class TestTimeConversion(unittest.TestCase):
    def test_01(self):
        self.assertEqual((12, 23), heads_and_legs(35, 94))

    def test_02(self):
        self.assertEqual((10, 0), heads_and_legs(10, 40))

    def test_03(self):
        self.assertEqual((0, 10), heads_and_legs(10, 20))

    def test_04(self):
        self.assertEqual((5, 5), heads_and_legs(10, 30))

    def test_05(self):
        self.assertEqual((0, 0), heads_and_legs(5, 15))

    def test_01(self):
        self.assertEqual((28, 44), heads_and_legs(72, 200))


if __name__ == '__main__':
    unittest.main()

