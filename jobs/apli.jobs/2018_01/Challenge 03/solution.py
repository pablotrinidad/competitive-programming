"""Heads and legs.

Write a program to solve this puzzle:
    We count 35 heads and 94 legs among the cats and
    parrots in a pet store. How many cats and how many
    parrots do we have?

It is possible that no solution can be found!

examples:
    heads_and_legs(10, 40) returns (10, 0)
    heads_and_legs(10, 20) returns (0, 10)
    heads_and_legs(10, 30) returns (5, 5)
    heads_and_legs(35, 94) returns (12, 23)
    heads_and_legs(5, 15) returns (0, 0)

"""


def heads_and_legs(heads, legs):
    """Heads and legs."""
    for i in range(0, heads + 1):
        if (i * 4) + ((heads - i) * 2) == legs:
            return (i, heads - i)
    return (0, 0)
