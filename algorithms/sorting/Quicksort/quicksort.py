"""Quicksort."""


def partition(A, p, r):
    """Find partition point."""
    x = A[r]
    i = p - 1
    for j in range(p, r):  # Without reaching r (non-inclusive)
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = x, A[i + 1]
    return i + 1


def quicksort(A, p, r):
    """Quicksort."""
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def sort(A):
    """Merge sort."""
    quicksort(A, 0, len(A) - 1)
    return A


import random  # NOQA

A = random.choices(range(1, 30), k=15)
print("Unsorted:\t", A)

A = sort(A)
print("Sorted:\t\t", A)
