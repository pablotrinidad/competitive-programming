"""InterviewBit.

Programming > Math > Excel Column Number
"""


class Solution:
    """Solution."""

    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        """Solution."""
        A = [e for e in A]
        number = 0
        for i in range(len(A)):
            base = 26 ** i
            number += (ord(A[- 1 - i]) - 64) * base
        return number


inputs = [
    "A",
    "B",
    "C",
    "Z",
    "AA",
    "AB",
    "AZ",
    "ZZZ",
    "AAA"
]

solution = Solution()
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.titleToNumber(*i))
    print('\n' * 2)
