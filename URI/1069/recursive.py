"""Diamonds extractor."""


def f(s, o=0):
    """Diamonds extractor."""
    if len(s) == 0:
        return 0
    elif s[0] == '<':
        return f(s[1:], o + 1)
    elif s[0] == '>' and o > 0:
        return 1 + f(s[1:], o - 1)
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(f(s))
