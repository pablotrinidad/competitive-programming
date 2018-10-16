"""Maximum square.

Have the function MaximumSquare(strArr) take the strArr parameter being passed which will be a 2D matrix
of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's.
A square submatrix is one of equal width and height, and your program should return the area of the
largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"]
then this looks like the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

For the input above, you can see that the largest square submatrix is of size 2x2, so your program should
return the area which is 4.
You can assume the input will not be empty.
"""


def get_max_n(p, l, n_limit):
    """Expand square trying to obtain the largest sub-matrix within bounds."""
    n = 1
    x = p[0]
    y = p[1]
    valid = True
    while valid:
        for i in range(n):
            if i == n-1:
                for j in range(n):
                    valid = int(l[x + i][y + j]) and valid
            else:
                valid = int(l[x + i][y + n - 1]) and valid
        if n + 1 <= n_limit:
            n += 1
        else:
            break

    return n if valid else n - 1


def maximum_square(m):
    """Maximum square."""
    s = len(m)
    n = 1
    for i in range(s):
        for j in range(s):
            if int(m[i][j]) == 1:
                n_limit = min((s - i), (s - j))
                max_n = get_max_n((i, j), m, n_limit)  # Create cell expansion
                if max_n > n:
                    n = max_n
    return n ** 2


print(
    maximum_square(["111", "111", "111"])
)
