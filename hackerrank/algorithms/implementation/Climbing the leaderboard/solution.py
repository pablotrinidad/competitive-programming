"""Solution.

HackerRank > Algorithms > Implementation > Climbing the leaderboard.
"""


def binary_search_index(L, v):
    """Return index where V should land."""
    left, right = 0, len(L) - 1

    if right == left:
        return 1

    while right > left:
        mid = left + (right - left) // 2
        if v == L[mid]:
            return mid + 1
        if v > L[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if left == mid:
            return left + 1 if L[mid] < v else left - 1
    if right == mid:
        return right + 1 if L[mid] < v else right - 1
    else:
        return left + 2 if v < L[left] else left + 1


def climb_leaderboard(scores, alice):
    """Return list of positions over Alice's ranking."""
    scores = list(set(scores))
    scores.sort(reverse=True)
    ranks = [binary_search_index(scores, s) for s in alice]
    return ranks


if __name__ == '__main__':
    n, scs = input(), [int(i) for i in input().split(' ')]
    m, alc = input(), [int(i) for i in input().split(' ')]
    ranks = climb_leaderboard(scs, alc)
    for rank in ranks:
        print(rank)
