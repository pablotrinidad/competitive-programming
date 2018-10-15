"""Sum of chars.

Write a program that sums the alphabet positions of the characters in a provided string.
Characters are treated case insensitive.

examples:
    sum_chars('ab') returns 3 (a=1, b=2)
    sum_chars('AbCd') returns 10 (a=1, b=2, c=3, d=4)
    sum_chars('Apli') returns 38

"""

from string import ascii_letters


def sum_chars(s):
    """Sum chars."""
    s = s.lower()
    return sum([(i + 1) * s.count(c) for i, c in enumerate(ascii_letters)])
