"""InterviewBit.

Programming > Arrays > K-th row of Pascal's Triangle.
"""


class Solution:
    """Solution."""

    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        """Get k-th row."""
        base = [1] + [0] * (A)
        row = [1] * (A + 1)
        for i in range(A + 1):
            for k in range(1, i):
                row[k] = base[k - 1] + base[k]
            base = row[:]
        return row


k = int(input())
row = Solution().getRow(k)
print(row)

