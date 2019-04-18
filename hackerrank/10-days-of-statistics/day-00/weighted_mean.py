input() # Ignore first line

# X values
s = input().split(' ')
X = [int(i) for i in s]

# W values
t = input().split(' ')
W = [int(i) for i in t]

weights_total = 0
total = 0
for i in range(len(X)):
    weights_total += W[i]
    total += W[i]*X[i]

print(round(total/weights_total, 1))