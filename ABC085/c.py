n, y = map(int, input().split())
ans = [-1, -1, -1]
flag = 0
for i in range(n+1):
    for j in range(n-i+1):
        temp = i * 10000 + j * 5000 + (n-i-j) * 1000
        if temp == y:
            ans = [i, j, n-i-j]
            falg = 1
            break
    if flag == 1:
        break

print(" ".join(map(str, ans)))
