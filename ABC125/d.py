n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    if a[i] < 0:
        count += 1
        a[i] = -1*a[i]

if count % 2 == 0:
    print(sum(a))
else:
    print(sum(a)-2*min(a))
