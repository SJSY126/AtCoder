n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a <= b:
        if b % a == 0:
            return a
        else:
            return(gcd(b % a, a))
    else:
        if a % b == 0:
            return b
        else:
            return(gcd(a % b, b))


ans = gcd(a[0], a[1])

for i in range(2, len(a)):
    ans = gcd(ans, a[i])

print(ans)
