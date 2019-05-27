menu = [int(input()) for _ in range(5)]

ans = 0
x = 10

for i in range(5):
    if menu[i] % 10 == 0:
        ans += menu[i]
    else:
        x = min(x, menu[i] % 10)
        ans += (menu[i] // 10 + 1)*10

ans -= 10-x

print(ans)
