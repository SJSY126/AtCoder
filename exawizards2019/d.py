n, x = map(int, input().split())
s = list(map(int, input().split()))

s.sort()
for i in range(n):
    if s[i] > x:
        s = s[0:i-1]

for
print(s)
