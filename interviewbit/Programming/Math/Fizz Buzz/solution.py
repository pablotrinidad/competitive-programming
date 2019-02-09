"""InterviewBit.

Programming > Math > Fizz Buzz.
"""


class Solution:
    """Solution."""

    def fizzBuzz(self, A):
        """Fizz Buzz."""
        R = []
        for i in range(1, A + 1):
            val = 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
            R.append(val if val else str(i))
        return R


solution = Solution()
N = 20
for i in range(1, N + 1):
    print(i, ':', solution.fizzBuzz(i))
