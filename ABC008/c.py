n = int(input())
c = [int(input()) for _ in range(n)]
ans = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if c[i] % c[j] == 0 and i != j:
            cnt += 1

    if cnt % 2 == 0:
        ans += (cnt+2)/(2*cnt+2)
    else:
        ans += 1/2

print(ans)
