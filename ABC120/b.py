a, b, k = map(int, input().split())
c = 1
i = 0
ans = []
while c <= min(a, b):
    if a % c == 0 and b % c == 0:
        ans.append(c)
        i += 1

    c += 1

print(ans[-k])
