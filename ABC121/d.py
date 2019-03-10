def f(n):
    x = n // 2

    if n % 2 == 0:
        if x % 2 == 0:
            return 0 ^ n
        else:
            return 1 ^ n

    else:
        x += 1
        if x % 2 == 0:
            return 0
        else:
            return 1


A, B = map(int, input().split())

print(f(A-1) ^ f(B))
