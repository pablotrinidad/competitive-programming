"""Cur rod.

Recursive top-down implementation.
"""


def cut_rod(p, n):
    """Cut rod.

    Implements the computation in the equation 15.2 (r_n = max_{i <= i <= n}(p_i + r_{n-1})).

    Where p is the array of prices by length and n the length of the rod.
    """
    if n == 0:
        return 0
    q = 0
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - (i + 1)))
    return q


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Figure 15.1

for i in range(1, 11):
    print("Test cur_rod for n=" + str(i))
    r = cut_rod(p, i)
    print("\t", r)
