n, k = map(int, input().split())
rate = list(map(int, input().split()))

ans = 0
rate.sort()

for i in range(n-k, n):
    ans = (rate[i] + ans) / 2

print(ans)
