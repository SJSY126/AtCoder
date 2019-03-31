n = int(input())
a = [0] * (n+1)

for i in range(1, n+1):
    a[i] = int(input())

s = set()
temp = 1
ans = -1
count = 0
while temp not in s:
    s.add(temp)
    count += 1
    if a[temp] != 2:
        temp = a[temp]
    else:
        ans = count
print(ans)
