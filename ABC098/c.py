n = int(input())
s = list(input())
ans = n
for i in range(n):
    if i == 0:
        ans = min(ans, s[1:].count("E"))
    elif i == n-1:
        ans = min(ans, s[:n-2].count("W"))
    else:
        ans = min(ans, s[:i-1].count("W")+s[i+1:].count("E"))
print(ans)
