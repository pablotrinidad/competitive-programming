"""InterviewBit.

Programming > Binary Search > Cont Element Occurence.
"""


class Solution:
    """Solution."""

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        """Return the number of occurrences of B in A."""
        start = 0
        end = len(A) - 1
        count = 0
        while start <= end:
            mid = (end + start) // 2
            if A[mid] == B:
                count += 1
                count += self.findCount(A[mid + 1: end + 1], B)
                count += self.findCount(A[start:mid], B)
                break
            if A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return count


import random  # NOQA

A = []
print("Contnt of A:")
for i in range(1, 10):
    n = random.randint(1, 100)
    A += [i] * n
    print("\t{} elements added with value {}".format(n, i))
B = random.randint(1, 9)
print("B:", B)

solution = Solution()
print(solution.findCount(A, B))
