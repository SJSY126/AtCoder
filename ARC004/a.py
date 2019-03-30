n = int(input())
a = [[0]*2 for _ in range(n)]
ans = 0

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        length = (a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2
        ans = max(ans, length**0.5)

print(ans)
