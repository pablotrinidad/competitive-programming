"""InterviewBit.

Programming > Binary Search > Rotated Array.
"""


class Solution:
    """Solution."""

    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        """Find pivot."""
        if len(A) == 1:
            return A[0]
        start = 0
        end = len(A) - 1
        n = len(A)
        while start <= end:
            mid = (end + start) // 2
            next_ = (mid + 1) % n
            prev_ = (mid + n - 1) % n
            if A[prev_] > A[mid] and A[next_] > A[mid]:
                return A[mid]
            if A[mid] > A[end]:
                start = mid + 1
            elif A[mid] < A[end]:
                end = mid - 1
        return -1


A = [5, 6, 7, 8, 9, 10, 2, 3, 4]
solution = Solution()
print(A)
print(solution.findMin(A))
