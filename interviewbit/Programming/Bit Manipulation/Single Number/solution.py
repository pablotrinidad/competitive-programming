"""InterviewBit.

Programming > Bit Manipulation > Single number.
"""

import operator
import functools


class Solution:
    """Solution."""

    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        """Solution."""
        return functools.reduce(operator.xor, A)


a = [1, 2, 2, 3, 1]
solution = Solution()
print(solution.singleNumber(a))
