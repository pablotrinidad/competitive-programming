import unittest
from solution import ClosestNeighbour

class TestClosestNeighbour(unittest.TestCase):
    def test_no_neighbour(self):
        strArr = ['000', '100', '000']
        self.assertEqual(0, ClosestNeighbour(strArr))

    def test_matrix_malformed(self):
        strArr = ['000', '100', '0000']
        self.assertEqual(0, ClosestNeighbour(strArr))

    def test_3by3_matrix(self):
        strArr = ['000', '100', '200']
        self.assertEqual(1, ClosestNeighbour(strArr))

    def test_4by4matrix(self):
        strArr = ['0000', '2010', '0000', '2002']
        self.assertEqual(2, ClosestNeighbour(strArr))

    def test_5by5_matrix(self):
        strArr = ['10000', '00022', '00020', '00000', '00200']
        self.assertEqual(2, ClosestNeighbour(strArr))

if __name__ == '__main__':
    unittest.main()
