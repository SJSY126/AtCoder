k, s = map(int, input().split())
count = 0

for i in range(k+1):
    for j in range(k+1):
        t = s - (i + j)
        if 0 <= t and t <= k:
            count += 1

print(count)
