input() # Ignore first line 
s = input().split(' ')
L = len(s)
N = sorted([int(i) for i in s])

median = N[L//2] if L % 2 != 0 else (N[(L//2) - 1] + N[L//2])/2 

total = 0
mode, mode_c = None, 0
cmode, cmode_c = None, 0
for n in N:
    total += n
    if cmode_c > mode_c:
        mode = cmode
        mode_c = cmode_c
    if n != cmode:
        cmode = n
        cmode_c = 0
    cmode_c += 1

print(total / L)  # Mean
print(median)  # Median
print(mode)