s = list(input())
n = int(input())
a = [[]*2]*n
for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    l, r = a[i]
    temp = s[l-1:r]
    temp.reverse()
    s = s[0:l-1] + temp + s[r:]

print(''.join(s))
