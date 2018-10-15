import unittest
from solution import militaryTime

class TestTimeConversion(unittest.TestCase):
    def test_01(self):
        self.assertEqual('00:04:57', militaryTime('12:04:57AM'))

    def test_02(self):
        self.assertEqual('12:23:14', militaryTime('12:23:14PM'))

    def test_03(self):
        self.assertEqual('21:17:39', militaryTime('09:17:39PM'))

    def test_04(self):
        self.assertEqual('07:14:21', militaryTime('07:14:21AM'))

if __name__ == '__main__':
    unittest.main()
