"""InterviewBit.

Programming > Arrays > Find Duplicate in Array.
"""


class Solution:
    """Solution."""

    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        """Repeated number."""
        B = [0] * len(A)
        for i in range(len(A)):
            B[A[i] - 1] += 1
            if B[A[i] - 1] > 1:
                return A[i]
        return -1


A = [3, 4, 1, 4, 1]
R = Solution().repeatedNumber(A)
print(A)
print(R)
