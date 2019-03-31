a, b, c = map(int, input().split())
ans = "NO"
for i in range(a, a*b+1, a):
    if c == i % b:
        ans = "YES"
        break

print(ans)
