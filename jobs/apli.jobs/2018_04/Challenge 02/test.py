import unittest
from solution import robot_attack

class Testrobot_attack(unittest.TestCase):
    def test_01(self):
        robots = [1, 2]
        self.assertEqual(1, robot_attack(robots))

    def test_02(self):
        robots = [3, 3, 3]
        self.assertEqual(5, robot_attack(robots))

    def test_03(self):
        robots = [3, 0, 3, 0, 3]
        self.assertEqual(9, robot_attack(robots))

    def test_04(self):
        robots = [7, 9, 1, 0, 8, 7]
        self.assertEqual(26, robot_attack(robots))

    def test_05(self):
        robots = [1, 0, 5, 0, 2, 0, 3, 3]
        self.assertEqual(12, robot_attack(robots))

    def test_06(self):
        robots = [4, 6, 9, 1, 1, 8, 7, 10, 10, 9, 2, 10, 5, 1, 4, 3, 4, 9, 7, 1]
        self.assertEqual(74, robot_attack(robots))

if __name__ == '__main__':
    unittest.main()
