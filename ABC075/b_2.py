h, w = map(int, input().split())
masu = [[0]*w for _ in range(h)]

for i in range(h):
    masu[i] = list(input())

for i in range(h):
    for j in range(w):
        if masu[i][j] == ".":
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    xx = j + dx
                    yy = i + dy
                    if 0 <= xx and xx < w and 0 <= yy and yy < h:
                        if masu[yy][xx] == "#":
                            count += 1
            masu[i][j] = count
for i in range(h):
    print("".join(map(str, masu[i])))
