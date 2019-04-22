d, g = map(int, input().split())
p = [0] * d
c = [0] * d
ans = 10000000000000000000000000000
for i in range(d):
    p[i], c[i] = map(int, input().split())

for i in range(2**d):
    sum = 0
    num = 0
    for j in range(d):
        if i & (1 << j):
            sum += c[j]+p[j]*100*(j+1)
            num += p[j]
    if sum >= g:
        ans = min(ans, num)
    else:
        for j in range(d-1, -1, -1):
            if i & (1 << j):
                continue
            for k in range(p[j]):
                if sum >= g:
                    break
                sum += 100*(j+1)
                num += 1
        ans = min(ans, num)
print(ans)
