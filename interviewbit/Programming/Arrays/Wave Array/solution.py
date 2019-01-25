"""InterviewBit.

Programming > Arrays > Wave Array
"""


class Solution:
    """Solution."""

    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        """Return waved array."""
        A = sorted(A)
        if len(A) % 2 == 0:
            return [A[i ^ 1] for i in range(len(A))]
        else:
            return [A[i ^ 1] for i in range(len(A) - 1)] + [A[-1]]
