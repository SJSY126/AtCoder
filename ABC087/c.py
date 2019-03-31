n = int(input())
a = [[0]*n]*2

for i in range(2):
    a[i] = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans = max(sum(a[0][:i+1])+sum(a[1][i:]), ans)
print(ans)
