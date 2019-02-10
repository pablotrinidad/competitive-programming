"""InterviewBit.

Programming > Math > Rearrange array.
"""


class Solution:
    """Solution."""

    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        """Solution."""
        n = len(A)
        for i in range(n):
            A[i] += (A[A[i]] % n) * n
        for i in range(n):
            A[i] = A[i] // n


import random  # NOQA

solution = Solution()
N = 10
inputs = [list(range(x)) for x in range(N)]
for i in inputs:
    random.shuffle(i)

for i in inputs:
    print("Input:", i)
    solution.arrange(i)
    print("Solution:", i, '\n')
