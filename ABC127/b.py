r, d, x_0 = map(int, input().split())

x = [0] * 11
x[0] = x_0

for i in range(10):
    x[i+1] = r * x[i] - d
    print(x[i+1])
