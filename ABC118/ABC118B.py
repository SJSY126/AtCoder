n, m = map(int, input().split())
l = [input().split() for i in range(n)]

x = set()

if len(l) == 1:
    print(len(l[0])-1)
else:
    x = set(l[0][1:])
    for i in range(1, len(l)):
        x = x & set(l[i][1:])
    print(len(x))
