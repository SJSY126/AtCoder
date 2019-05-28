n = int(input())
a = list(map(int, input().split()))
b = [0]*(2+max(a))

for i in range(n):
    b[a[i]] += 1

ans = 0

for i in range(len(b)):
    if b[i] != 0:
        ans = max(ans, b[i-1]+b[i]+b[i+1])
print(ans)
