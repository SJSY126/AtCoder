n = int(input())
a = [0]*(n+1)
b = [0]*(n+1)

for i in range(1, n+1):
    a[i], b[i] = map(int, input().split())
