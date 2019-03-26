n = int(input())
a = {}

for i in range(n):
    b = input()
    if b not in a:
        a[b] = 1
    else:
        a[b] += a[b]
a = sorted(a.items(), key=lambda x: x[1])

print(a[-1][0])
