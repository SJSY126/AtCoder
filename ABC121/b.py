N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [[0*M]]*N
ans = 0
for i in range(N):
    x = 0
    A[i] = list(map(int, input().split()))
    for j in range(M):
        x += A[i][j] * B[j]

    x += C

    if x > 0:
        ans += 1


print(ans)
