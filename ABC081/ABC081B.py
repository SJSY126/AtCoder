
"""ABC081B.py."""

n = int(input())
a = list(map(int, input().split()))

count = 0
go = 1

while go:
    for i in range(n):
        if a[i] % 2 == 1:
            go = 0
        else:
            a[i] = a[i] / 2

    count = count + 1

print(count-1)
