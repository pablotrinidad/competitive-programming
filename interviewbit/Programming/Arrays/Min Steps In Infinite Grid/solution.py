"""InterviewBit.

Programming > Arrays > Min Steps In Infinite Grid.
"""


class Solution:
    """Solution."""

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        """Cover points."""
        x, y = A[0], B[0]
        steps = 0
        for xf, yf in zip(A, B):
            dx, dy = abs(x - xf), abs(y - yf)
            steps += max(dx, dy)
            x, y = xf, yf
        return steps

