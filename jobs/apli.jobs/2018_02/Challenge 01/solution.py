"""Closes Neighbor.

Have the function ClosestNeighbour(strArr) read the matrix of numbers stored in strArr which
will be a 2D matrix that contains only the integers 1, 0, or 2.
Then from the position in the matrix where a 1 is, return the number of spaces either left,
right, down, or up you must move to reach an enemy which is represented by a 2.
You are able to wrap around one side of the matrix to the other as well.

For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from
the 1 by moving left to wrap to the other side and then moving down once.
The array can contain any number of 0's and 2's, but only a single 1.
It may not contain any 2's at all as well, where in that case your program should return a 0.

The program should also return 0 if the matrix is malformed, meaning the column count is not the
same in all rows.
"""


def closest_neighbor(m):
    """Closest neighbor."""
    if sum([len(x) for x in m]) != len(m) ** 2:
        return 0

    s = len(m)
    twos = []
    one = ()

    # Scan map
    for i in range(s):
        for j in range(s):
            if int(m[i][j]) == 2:
                twos.append((i, j))
            elif int(m[i][j]) == 1:
                one = (i, j)

    # No enemies found
    if not twos:
        return 0

    # Compute distances
    shortest_route = 2 * s
    for t in twos:
        dx = 1 if abs(t[0] - one[0]) == (s - 1) else abs(t[0] - one[0])
        dy = 1 if abs(t[1] - one[1]) == (s - 1) else abs(t[1] - one[1])
        d = dx + dy
        if d < shortest_route:
            shortest_route = d

    return shortest_route
