"""Solution.

HackerRank > Algorithms > Greedy > Mark and Toys
"""


def maximumToys(prices, k):
    """Problem solution."""
    prices.sort()
    c = 0
    for toy in prices:
        if toy > k:
            return c
        else:
            k -= toy
            c += 1
    return c
