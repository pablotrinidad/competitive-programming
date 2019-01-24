"""Insertion sort implementation."""


def sort(A):
    """Insertion sort."""
    for i in range(1, len(A)):
        e = A[i]
        j = i - 1
        while j >= 0 and A[j] > e:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = e
    return A


import random  # NOQA

A = random.choices(range(1, 16), k=10)
print(A)

A = sort(A)
print(A)
