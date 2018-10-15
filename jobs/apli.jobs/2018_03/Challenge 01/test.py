import unittest
from solution import ScaleBalancing

class ScaleBalancingTestCase(unittest.TestCase):
    def test_01(self):
        tplWeights = ([10, 5], [2, 4, 6])
        self.assertEqual([], ScaleBalancing(tplWeights))

    def test_02(self):
        tplWeights =  ([3, 4], [1, 2, 7, 7])
        self.assertEqual([1], ScaleBalancing(tplWeights))

    def test_03(self):
        tplWeights = ([13, 4], [1, 2, 3, 6, 14])
        self.assertEqual([3, 6], ScaleBalancing(tplWeights))

    def test_04(self):
        tplWeights = ([5, 9], [1, 2, 6, 7])
        self.assertEqual([2, 6], ScaleBalancing(tplWeights))


if __name__ == '__main__':
    unittest.main()
