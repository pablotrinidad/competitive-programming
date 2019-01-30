"""InterviewBit.

Programming > Arrays > Add One To Number.
"""


class Solution:
    """Solution."""

    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        """Plus one."""
        # Remove leading zeros
        while A[0] == 0 and len(A) > 1:
            A = A[1:]

        # Handle decimal "upgrade"
        i = len(A) - 1
        remaining = (A[i] + 1) % 10
        while i > 0 and remaining == 0:
            A[i] = 0
            i -= 1
            remaining = (A[i] + 1) % 10

        # Handle last update
        if A[i] < 9:
            A[i] = A[i] + 1
        else:
            A = [1, 0] + A[1:]

        # Return new digit
        return A


# A = [0]
# A = [0, 3, 7, 6, 4, 0, 5, 5, 5]
# A = [9, 9]
A = [0, 9, 5, 7, 4, 9, 7, 7]
R = Solution().plusOne(A)
print(R)
