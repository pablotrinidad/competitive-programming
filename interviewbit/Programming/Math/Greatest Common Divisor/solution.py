"""InterviewBit.

Programming > Math > Greatest common divisor
"""


class Solution:
    """Solution."""

    def gcd(self, A, B):
        """Solution."""
        if 0 in [A, B]:
            return max(A, B)

        while A != B:
            if A > B:
                A -= B
            else:
                B -= A
        return A


inputs = [
    [3, 9],
    [3, 6],
    [1, 1],
    [0, 2],
    [318, 246]
]

solution = Solution()
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.gcd(*i))
    print('\n' * 2)
