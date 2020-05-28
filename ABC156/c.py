n = int(input())
x = list(map(int, input().split()))
p = round(sum(x)/n)

ans = 0
for xi in x:
    ans += (xi - p) ** 2

print(ans)
