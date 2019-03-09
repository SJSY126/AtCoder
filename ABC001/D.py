def round(x): return (x*2+1)//2


def time_start(x):
    a = x % 10
    if 0 <= a and a < 5:
        x -= a
    else:
        x -= (a-5)
    return x


def time_end(x):
    a = x % 5
    if a == 0:
        pass
    else:
        x += (5-a)
    return x


n = int(input())
t = [[]*2] * n
for i in range(n):
    t[i] = list(map(int, input().split("-")))
    t[i][0] = time_start(t[i][0])

    if time_end(t[i][1]) % 100 == 60:
        t[i][1] = int((t[i][1]//100) * 100 + 100)
    else:
        t[i][1] = int(time_end(t[i][1]))

t.sort()


for i in range(len(t)-1):
    if t[i][1] < t[i+1][0]:
        pass
    elif t[i][1] >= t[i+1][0]:
        t[i + 1] = [t[i][0], max(t[i][1], t[i+1][1])]
        t[i] = [0, 0]

for i in range(len(t)):
    if t[i] != [0, 0]:
        s = 4 - len(str(t[i][0]))
        e = 4 - len(str(t[i][1]))
        print("0"*s + str(t[i][0]) + "-" + "0"*e + str(t[i][1]))
