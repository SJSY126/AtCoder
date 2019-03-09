"""ABC083B."""

n, a, b = map(int, input().split())
sum = 0


for m in range(10):
    for k in range(10):
        for j in range(10):
            for i in range(10):
                for o in range(2):
                    if 1 * i + 10 * j + 100 * k + 1000 * m + 10000 * o <= n:
                        if (i + j + k + m + o) >= a and (i + j + k + m + o) <= b:
                            sum += 1 * i + 10 * j + 100 * k + 1000 * m + 10000 * o

print(sum)
