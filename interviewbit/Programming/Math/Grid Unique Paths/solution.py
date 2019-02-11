"""InterviewBit.

Programming > Math > Grid Unique Paths
"""


class Solution:
    """Solution."""

    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        """Solution."""
        grid = [[1] * B] * A
        for i in range(1, A):
            for j in range(1, B):
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[A-1][B-1]


inputs = [
    [1, 1],
    [1, 10],
    [10, 1],
    [2, 2],
    [3, 3],
    [5, 5],
    [10, 5],
    [15, 9]
]

solution = Solution()
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.uniquePaths(*i), '\n')
