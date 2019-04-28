n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

diff = [0]*n

for i in range(n):
    if v[i] - c[i] > 0:
        diff[i] = v[i] - c[i]

print(sum(diff))
