n, q = map(int, input().split())
s = input()
d = {}
mask = {}
for i in range(n):
    if s[i] not in d:
        d[s[i]] = [0]*n
        mask[s[i]] = [0]*n
    d[s[i]][i] = 1
    mask[s[i]][i] = 1
ans = 0

for i in range(q):
    moji, cmd = input().split()
    if moji not in d:
        continue
    if cmd == "R":
        d[moji] = [0] + d[moji][0:n-1]
    elif cmd == "L":
        d[moji] = d[moji][1:] + [0]
    masu = [0]*n
    for k, v in d.items():
        for j in range(n):
            masu[j] += d[k][j]
    if i < q-1:
        for k, v in d.items():
            for j in range(n):
                d[k][j] = mask[k][j] * masu[j]
ans = 0
for k, v in d.items():
    ans += sum(v)
print(ans)
