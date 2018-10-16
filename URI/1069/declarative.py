"""Diamonds extractor."""


def extract_diamonds(s):
    """Diamonds extractor."""
    d = 0
    i = 0
    last_o = None
    last_c = None
    while i < len(s) and len(s) > 1:
        if s[i] == '<':
            last_o = i
        elif s[i] == '>' and last_o is not None:
            last_c = i

        if last_o is not None and last_c is not None:
            s = s[0:last_o] + s[last_c + 1:]
            d += 1
            i = 0
            last_o = None
            last_c = None
        else:
            i += 1
    return d


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(extract_diamonds(s))
