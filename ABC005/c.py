t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ai = 0
bi = 0

while ai < n and bi < m:
    A = a[ai]
    B = b[bi]

    if A <= B <= A + t:
        ai += 1
        bi += 1
    else:
        ai += 1

if bi == m:
    print("yes")
else:
    print("no")
