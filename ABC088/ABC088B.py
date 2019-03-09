n = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()

i = 0
Alice_point = 0
Bob_point = 0

while 1:
    Alice_point += a[i]
    i += 1
    if i >= n:
        break
    Bob_point += a[i]
    i += 1
    if i >= n:
        break

print(Alice_point - Bob_point)
