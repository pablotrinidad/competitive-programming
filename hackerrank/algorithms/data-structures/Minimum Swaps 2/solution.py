"""Solution.

HackerRank > Algorithms > Data Structures > Minimum Swaps 2
"""


def distance(L):
    """Return each element's distance from its corresponding location."""
    return [abs(L[i] - i - 1) for i in range(len(L))]  # O(n)


def minimum_swaps(L):
    """Return the minimum swaps needed."""
    swaps = 0
    curr_distance = distance(L)
    c = len(L)
    all_ones = False
    while sum(curr_distance) > 0 and c > 0 and not all_ones:
        print("List:", L)
        print("Dist:", curr_distance)
        print("Swaps:", swaps)
        # If every number is at distance one of location, result can be returned analytically.
        ones_count, all_ones = 0, True
        for d in curr_distance:
            all_ones = all_ones and True if d in (1, 0) else False
            ones_count += 1 if d == 1 else 0
        if all_ones:
            return swaps + (ones_count // 2)

        max_1 = 0  # Will stick to the left
        max_2 = 1  # Will try to reach right-most max

        for i in range(2, len(L)):
            if curr_distance[i] >= curr_distance[max_1] or curr_distance[i] >= curr_distance[max_2]:
                print('\tMAX1 at index', max_1, ':', curr_distance[max_1])
                print('\tMAX2 at index', max_2, ':', curr_distance[max_2])
                if curr_distance[i] > curr_distance[max_1]:
                    max_1, max_2 = i, max_1
                else:
                    max_2 = i
                print('\t---\n\tMAX1 at index', max_1, ':', curr_distance[max_1])
                print('\tMAX2 at index', max_2, ':', curr_distance[max_2])
                print(max_1, max_2)
        L[max_1], L[max_2] = L[max_2], L[max_1]
        swaps += 1
        curr_distance = distance(L)
        c -= 1
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = [int(e) for e in input().strip().split()]
    r = minimum_swaps(arr)
    print(r)
