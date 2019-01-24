"""Merge sort."""


def merge(L, R):
    """Merge lists."""
    A = []
    while len(L) > 0 and len(R) > 0:
        if L[0] >= R[0]:
            A.append(R.pop(0))
        elif L[0] < R[0]:
            A.append(L.pop(0))
    return A + L + R


def sort(A):
    """Merge sort."""
    n = len(A)
    if n <= 1:
        return A

    left, right = sort(A[:n // 2]), sort(A[n // 2:])
    A = merge(left, right)

    return A


import random  # NOQA

A = random.choices(range(1, 30), k=15)
print("Unsorted:\t", A)

A = sort(A)
print("Sorted:\t\t", A)
