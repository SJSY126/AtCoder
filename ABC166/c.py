N, M = map(int, input().split())

H = list(map(int, input().split()))
ma = [0 for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    ma[A - 1] = max(ma[A - 1], H[B - 1])
    ma[B - 1] = max(ma[B - 1], H[A - 1])

ans = 0
for i in range(N):
    ans += H[i] > ma[i]

print(ans)
