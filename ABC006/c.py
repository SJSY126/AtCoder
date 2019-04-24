n, m = map(int, input().split())

ans = False

for i in range(n+1):
    for j in range(2):
        if m == 2 * i + 3*j+4*(n - i-j) and n - i-j >= 0:
            ans = True
            print(i, j, n-i-j)
            break
    if ans and True:
        break

if not ans:
    print(-1, -1, -1)
