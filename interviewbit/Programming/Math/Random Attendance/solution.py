"""InterviewBit.

Programming > Math > Grid Unique Paths
"""

import math


class Solution:
    """Solution."""

    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        """Solution."""
        print("UNSOLVED!!!!!")
        return self.digits(A)

    def digits(self, x):
        """Return list of digits of given x, assume x is encoded in base 10."""
        digits = []
        degree = int(math.log10(x))
        for i in range(degree, -1, -1):
            digits.append(x // 10**i)
            x = x % 10**i
        return digits


inputs = [
    [28829492, [1, 2]]
]

solution = Solution()
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.solve(*i), '\n')
