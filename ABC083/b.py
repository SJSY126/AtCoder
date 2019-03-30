def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


n, a, b = map(int, input().split())
s = [0]*5
ans = 0
for i in range(n+1):
    temp = sum_digits(i)
    if a <= temp and temp <= b:
        ans += i
print(ans)
