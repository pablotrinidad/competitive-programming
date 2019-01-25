"""InterviewBit.

Programming > Arrays > Set matrix zeros.
"""


class Solution:
    """Solution."""

    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        """Set zeros."""
        m, n = len(A), len(A[0])
        rows = [0] * m
        cols = [0] * n
        for row in range(m):
            for col in range(n):
                if A[row][col] == 0:
                    rows[row] = 1
                    cols[col] = 1

        for row in range(m):
            for col in range(n):
                if rows[row] == 1 or cols[col] == 1:
                    A[row][col] = 0
        return A


A = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1],
]
for y in A:
    print(' '.join([str(_) for _ in y]))

R = Solution().setZeroes(A)
print('\n')
for y in R:
    print(' '.join([str(_) for _ in y]))

