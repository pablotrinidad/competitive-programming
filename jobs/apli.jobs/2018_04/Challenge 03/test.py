import unittest
from solution import will_we_survive

class Testrobot_attack(unittest.TestCase):
    def test_01(self):
        robots = [1, 2]
        distance = 25
        self.assertEqual(True, will_we_survive(robots, distance))

    def test_02(self):
        robots = [3, 3, 3]
        distance = 100
        self.assertEqual(False, will_we_survive(robots, distance))

    def test_03(self):
        robots = [3, 0, 3, 0, 3]
        distance = 200
        self.assertEqual(True, will_we_survive(robots, distance))

    def test_04(self):
        robots = [7, 9, 1, 0, 8, 7]
        distance = 500
        self.assertEqual(False, will_we_survive(robots, distance))

    def test_05(self):
        robots = [1, 0, 5, 0, 2, 0, 3, 3]
        distance = 250
        self.assertEqual(True, will_we_survive(robots, distance))

    def test_06(self):
        robots = [4, 6, 9, 1, 1, 8, 7, 10, 10, 9, 2, 10, 5, 1, 4, 3, 4, 9, 7, 1]
        distance = 1450
        self.assertEqual(False, will_we_survive(robots, distance))


if __name__ == '__main__':
    unittest.main()
