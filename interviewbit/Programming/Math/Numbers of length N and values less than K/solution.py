"""InterviewBit.

Programming > Math > Numbers of length N and value less than K.
"""


class Solution:
    """Solution."""

    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        """Solution."""
        C = [int(i) for i in str(C)]
        if len(C) < B or len(A) < B:
            return 0
        if len(C) > B:
            n = len(A)
            return (n - 1) * (n**(B - 1)) if 0 in A else n**B

        if B == 1:
            return sum([1 for d in A if d < C[0]])

        dp, lower = [0] * (B + 1), [0] * 11
        dp[1] = sum([1 for d in A if d < C[0] and d != 0])

        for digit in A:
            lower[digit + 1] = 1
        for i in range(2, 11):
            lower[i] = lower[i - 1] + lower[i]

        equal_digits = True
        for i in range(2, B + 1):
            lower_digits = lower[C[i - 1]]
            dp[i] = dp[i - 1] * len(A)

            if equal_digits:
                dp[i] += lower_digits

            equal_digits = equal_digits & lower[C[i - 1] + 1] == lower[C[i - 1]] + 1

        return dp[B]


inputs = [
    [[0], 1, 5],
    [[0, 1, 2, 5], 1, 123],
    [[0, 1, 2, 5], 2, 21],
    [[2], 5, 54167],
    [[0, 3, 5, 6, 7], 5, 86344],  # 2500
    [[2, 3, 5, 6, 7, 9], 5, 42950],  # 2592
    [[0, 2, 3, 4, 5, 7, 8, 9], 5, 86587]  # 23040
]

solution = Solution()
for i in inputs:
    print("Input:", i)
    print("Solution:", solution.solve(*i))
    print('\n' * 2)
