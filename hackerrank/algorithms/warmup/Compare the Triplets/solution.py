"""Solution.

HackerRank > Algorithms > Warmup > Compare the Triplets.
"""


def compareTriplets(a, b):
    """Problem solution."""
    ap, bp = 0, 0
    for i in range(len(a)):
        ap += 1 if a[i] > b[i] else 0
        bp += 1 if b[i] > a[i] else 0
    return [ap, bp]
