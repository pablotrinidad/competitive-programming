"""Diamonds extractor."""


def f(s, i=0, o=None, c=None):
    """Diamonds extractor."""
    if i >= len(s):
        return 0
    if s[i] == '<':
        o = i
    elif s[i] == '>' and o is not None:
        c = i

    if o is not None and c is not None:
        return 1 + f(s[0:o] + s[c + 1:], i=0, o=None, c=None)
    else:
        return f(s, i+1, o, c)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(f(s))
