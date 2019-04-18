n = int(input())
X = sorted([int(s) for s in input().split(' ')])
F = [int(s) for s in input().split(' ')]

# Locate quartile indexes
total = sum(F)
Q1_index = total / 4
Q3_index = Q1_index * 3


Q1, Q3 = None, None
local_sum = 0
for i in range(n):
    local_sum += F[i]

    # Q1
    if not Q1:
        if local_sum >= Q1_index:
            print("Local sum:", local_sum)
            Q1 = 1

print('\n', '*' * 10)
print("Q1_index:", Q1_index)
print("Q3_index:", Q3_index)
print("Q1:", Q1)
print("Q3:", Q3)