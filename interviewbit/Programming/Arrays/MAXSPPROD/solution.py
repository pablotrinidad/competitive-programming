"""InterviewBit.

Programming > Arrays > MAXSPPROD.
"""


class Solution:
    """Solution."""

    def produce_specials(self, A):
        """Return "left-special" values."""
        stack = []
        specials = []
        for i in range(len(A)):
            while len(stack) > 0 and stack[-1][0] <= A[i]:
                stack.pop()
            if len(stack) == 0:
                specials.append(len(A))
            else:
                specials.append(stack[-1][1])
            stack.append((A[i], i))
        return specials

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        """Return max special product."""
        left_specials = [i if i < len(A) else 0 for i in self.produce_specials(A)]  # NOQA
        right_specials = [len(A) - i - 1 if i < len(A) else 0 for i in self.produce_specials(A[::-1])[::-1]]  # NOQA
        R = [l * r for l, r in zip(left_specials, right_specials)]
        return max(R) % 1000000007


# A = [ 7, 5, 7, 9, 8, 7 ]
A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
print(A)
R = Solution().maxSpecialProduct(A)
print(R)
