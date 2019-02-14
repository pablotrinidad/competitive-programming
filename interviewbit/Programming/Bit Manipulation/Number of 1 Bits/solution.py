"""InterviewBit.

Programming > Bit Manipulation > Number of 1 Bits.
"""


class Solution:
    """Solution."""

    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        """Solution."""
        zeros = 0
        while A > 0:
            zeros += 1
            A &= A - 1
        return zeros


inputs = [
    10, 24, 124, 3481, 204, 1, 0, 159, 30
]
solution = Solution()
for i in inputs:
    print('Input:', i, '\tBin:', bin(i)[2:])
    print('Solution:', solution.numSetBits(i))
