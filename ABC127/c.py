n, m = map(int, input().split())

l = [0]*m
r = [0]*m

mi = 1
ma = n + 1

for i in range(m):
    l[i], r[i] = map(int, input().split())
    mi = max(mi, l[i])
    ma = min(ma, r[i])

ans = ma - mi + 1

if ans >= 0:
    print(ans)
else:
    print(0)
