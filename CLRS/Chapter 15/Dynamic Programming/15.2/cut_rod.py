"""Rod cutting.

Recursive top-down implementation.
"""

import cProfile
from random import randint


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


def cut_rod2(p, n, r={}):
    """Cut rod.

    Same functionality as the original but implemented
    as a top-down with memoization.
    """
    q = r.get(n, None)
    if q:
        return q
    else:
        if n == 0:
            return 0
        else:
            q = 0
            for i in range(n):
                q = max(q, p[i] + cut_rod2(p, n - (i + 1), r))
            r[n] = q
            return q


def test_algorithms(n):
    """Test algorithms with n-sized problems."""
    p = [randint(1, 50) for _ in range(n)]
    for i in range(1, n+1):
        print('\n\n', '=' * 20, 'N:', i, '=' * 20)
        cProfile.runctx('cut_rod2(p, i)', globals(), locals())
        cProfile.runctx('cut_rod(p, i)', globals(), locals())

test_algorithms(25)
