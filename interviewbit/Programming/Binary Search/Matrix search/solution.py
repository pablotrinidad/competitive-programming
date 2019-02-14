"""InterviewBit.

Programming > Binary Search > Matrix search.
"""


class Solution:
    """Solution."""

    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        """Solution."""
        rows = len(A)
        cols = len(A[0])
        row, start, end = None, 0, rows - 1

        # Find row
        while start <= end:
            mid = (start + end) // 2
            if A[mid][0] == B:
                return 1

            if A[mid][0] < B and A[mid][-1] >= B:
                row = mid
                break
            if A[mid][0] > B:
                end = mid - 1
            else:
                start = mid + 1

        if row == None:
            return 0

        # Search in row
        start, end = 0, cols - 1
        while start <= end:
            mid = (start + end) // 2
            if A[row][mid] == B:
                return 1
            elif A[row][mid] > B:
                end = mid - 1
            else:
                start = mid + 1

        return 0


A = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
B = 50
print(Solution().searchMatrix(A, B))
