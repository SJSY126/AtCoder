def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)


n = int(input())
a = list(map(int, input().split()))
a = [0]+a[:]+[0]

l = [0]*len(a)
r = [0]*len(a)

for i in range(len(a)-1):
    m = len(a)-1
    l[i+1] = gcd(l[i], a[i+1])
    r[m-i-1] = gcd(r[m-i], a[m-i-1])

ans = [0]*n

for i in range(n):
    ans[i] = gcd(l[i], r[i+2])

print(max(ans))
