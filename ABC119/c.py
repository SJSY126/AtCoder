n, a, b, c = map(int, input().split())
l = [0]*n
mp = 0

flag = [a, b, c]
diff = [[-1]*n, [2]*n, [3]*n]

for i in range(n):
    l[i] = int(input())
    diff[0][i] = abs(a-l[i])
    diff[1][i] = abs(b - l[i])
    diff[2][i] = abs(c - l[i])

print(diff)

if flag == [0, 0, 0]:
    print(mp)
