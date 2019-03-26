def toribo(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        a = 0
        b = 0
        c = 1
        for i in range(3, n):
            d = (a + b + c) % 10007
            a, b, c = b, c, d
        return d


n = int(input())
print(toribo(n))
