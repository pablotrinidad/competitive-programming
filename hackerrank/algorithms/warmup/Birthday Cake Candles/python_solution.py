"""Birthday cake candles."""

n = input()
l = input()

l = [int(x) for x in l.split(' ')]

print(l.count(max(l)))
