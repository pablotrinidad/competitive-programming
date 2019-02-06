"""Solution.

HackerRank > Algorithms > Implementation > Beautiful Days at the Movies.
"""


def beautifulDays(i, j, k):
    """Problem solution."""
    def reverse(n):
        return int(str(n)[::-1])
    c = 0
    for day in range(i, j + 1):
        if (day - reverse(day)) % k == 0:
            c += 1
    return c
