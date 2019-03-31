def count_of_div(n):
    ret = 0
    while n % 2 == 0:
        n /= 2
        ret += 1
    return ret


n = int(input())
a = list(map(int, input().split()))
ans = min(map(count_of_div, a))
print(ans)
