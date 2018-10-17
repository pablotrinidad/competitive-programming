"""Diamonds extractor."""


def extract_diamonds(s):
    """Diamonds extractor."""
    d = 0
    o = 0
    for c in s:
        if c == '<':
            o += 1
        elif (c == '>') and (o > 0):
            d += 1
            o -= 1
    return d


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(extract_diamonds(s))
