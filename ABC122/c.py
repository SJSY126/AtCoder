n, q = map(int, input().split())
s = list(input())
b = [[]*2 for _ in range(q)]
for i in range(q):
    b[i] = list(map(int, input().split()))

c = [0 for _ in range(len(s))]
count = 0

for i in range(len(s)):
    if s[i:i+2] == ["A", "C"]:
        count += 1
        c[i:i+2] = [count-1, count]
    else:
        c[i:i+2] = [count, count]

for i in range(q):
    start = b[i][0]-1
    end = b[i][1]-1
    ans = c[end] - c[start]
    print(ans)
