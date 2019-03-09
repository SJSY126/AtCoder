n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

d = [-1]*(n+1)
d[0] = 0

for i in range(n+1):
    for ai in a:
        if (i - c[ai]) >= 0:
            d[i] = max(d[i], d[i-c[ai]]*10 + ai)
            print(d)

print(d[-1])
