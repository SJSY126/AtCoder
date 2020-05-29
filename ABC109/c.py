import functools
import numpy as np

n, X = map(int, input().split())
x = list(map(int, input().split()))


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


if n > 1:
    if abs(x[0]-X) == 0:
        ans = euclid(abs(x[1]-X), abs(x[2]-X))
    elif abs(x[1]-X) == 0:
        ans = euclid(abs(x[0]-X), abs(x[2]-X))
    else:
        ans = euclid(abs(x[0]-X), abs(x[1]-X))

    for xi in x[2:]:
        ans = euclid(ans, abs(xi-X))
        if ans == 1:
            break

else:
    ans = abs(x[0] - X)

print(ans)
