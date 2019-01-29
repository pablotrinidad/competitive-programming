"""Solution.

Algorithms > Strings > Weighted Uniform Strings
"""

import os


def weighted_uniform_strings(s, queries):
    """Given a string s, and a list of weight queries return a list indicating if query is possible."""
    weights = []
    last_char, repetitions = None, 1
    for c in s:
        val = ord(c) - 96
        if last_char == val:
            repetitions += 1
        else:
            repetitions = 1
        weights.append(val * repetitions)
        last_char = val

    weights = set(weights)
    results = []
    for q in queries:
        results.append('Yes' if q in weights else 'No')
    return results


# Provided by HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weighted_uniform_strings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
