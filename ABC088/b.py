n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice = sum(a[0::2])
Bob = sum(a[1::2])
print(Alice-Bob)
