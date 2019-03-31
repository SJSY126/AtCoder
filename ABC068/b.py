def count_of_divide_2(n):
    ret = 0
    while n % 2 == 0:
        n /= 2
        ret += 1
    return ret


n = int(input())
ans = 1
for i in range(1, n+1):
    if count_of_divide_2(ans) < count_of_divide_2(i):
        ans = i

print(ans)
