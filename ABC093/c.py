n = int(input())
a = [0 for _ in range(n+2)]
a[1:-1] = list(map(int, input().split()))
total = 0
for i in range(n + 1):
    total += abs(a[i+1]-a[i])

for i in range(1, n + 1):
    print(total-abs(a[i]-a[i-1])-abs(a[i+1]-a[i])+abs(a[i+1]-a[i-1]))
