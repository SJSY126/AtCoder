n = int(input())
a = set()

for i in range(n):
    a.add(int(input()))
ans = sorted(list(a), reverse=True)[1]
print(ans)
