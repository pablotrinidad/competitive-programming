input() # Ignore first input
s = input().split(' ')
X = sorted([int(i) for i in s])

def get_median(X):
    mid = len(X) // 2
    if len(X) % 2 == 0:
        return (X[mid - 1] + X[mid]) // 2
    return X[mid]

mid = len(X) // 2
print(get_median(X[:mid]))
print(get_median(X))
print(get_median(X[mid:]) if len(X) % 2 == 0 else get_median(X[mid+1:]))