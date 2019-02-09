"""InterviewBit.

Programming > Arrays > Rotate Matrix.
"""


class Solution:
    """Solution."""

    def rotate(self, A):
        """Rotate matrix."""
        n = len(A)
        for l in range(0, n // 2):  # l = level
            for o in range(0, n - (l * 2) - 1):  # o = offset
                tlr, tlc = l, l + o  # Top Left row/column
                trr, trc = l + o, n - 1 - l  # Top Right row/column
                brr, brc = n - 1 - l, n - 1 - l - o  # Bottom right row/column
                blr, blc = n - 1 - l - o, l  # Bottom left row/column

                # Switch corner values
                A[tlr][tlc], A[trr][trc], A[brr][brc], A[blr][blc] = A[blr][blc], A[tlr][tlc], A[trr][trc], A[brr][brc]
        return A


matrices = [
    [
        [1]
    ],
    [
        [1, 2],
        [3, 4]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p'],
    ],
    [
        [str(x).zfill(2) for x in range(1, 6)],
        [str(x).zfill(2) for x in range(6, 11)],
        [str(x).zfill(2) for x in range(11, 16)],
        [str(x).zfill(2) for x in range(16, 21)],
        [str(x).zfill(2) for x in range(21, 26)]
    ],
    [
        [str(x).zfill(2) for x in range(1, 7)],
        [str(x).zfill(2) for x in range(7, 13)],
        [str(x).zfill(2) for x in range(13, 19)],
        [str(x).zfill(2) for x in range(19, 25)],
        [str(x).zfill(2) for x in range(25, 31)],
        [str(x).zfill(2) for x in range(31, 37)]
    ]
]

solution = Solution()
for matrix in matrices:
    print("Matrix before rotation:")
    for row in matrix:
        print('\t', row)
    print("Matrix after rotation:")
    for row in solution.rotate(matrix):
        print('\t', row)
    print('\n' * 3)
