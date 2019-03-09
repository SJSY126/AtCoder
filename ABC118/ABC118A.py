A, B = map(int, input().split())

if B % A == 0:
    x = A+B
else:
    x = B-A
print(x)
