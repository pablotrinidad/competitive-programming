"""InterviewBit.

Programming > Math > Palindrome Integer.
"""

import math


class Solution:
    """Solution."""

    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        """Solution."""
        order = int(math.log10(A) + 1)
        while A > 0:
            if A % 10 != A // (10 ** (order - 1)):
                return 0
            A = A % (10 ** (order - 1)) // 10
            order -= 2
        return 1


solution = Solution()
inputs = [
    12121,
    123,
    2222,
    1,
    1111,
    12344321,
    12354321,
    123464321,
]
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.isPalindrome(i))
    print('\n' * 2)
