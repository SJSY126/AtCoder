N, M = map(int, input().split())
a = [[0*2]]*N
ans = 0
for i in range(N):
    a[i] = list(map(int, input().split()))

a.sort()
i = 0

while M > 0:
    if M - a[i][1] >= 0:
        ans += a[i][0] * a[i][1]
        M -= a[i][1]
    else:
        ans += a[i][0] * M
        M = 0
    i += 1


print(ans)
