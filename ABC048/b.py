def count_multiple(n, x):
    return n // x


a, b, x = map(int, input().split())
print(count_multiple(b, x)-count_multiple(a-1, x))
