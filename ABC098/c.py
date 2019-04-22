n = int(input())
s = list(input())
w = [0] * (n+1)
e = [0] * (n+1)
ans = n
for i in range(n):
    if s[i] == "W":
        w[i+1] = w[i] + 1
    else:
        w[i+1] = w[i]

for i in range(n-1, -1, -1):
    if s[i] == "E":
        e[i] = e[i+1] + 1
    else:
        e[i] = e[i+1]

for i in range(1, n+1):
    ans = min(ans, w[i-1]+e[i])
print(ans)
