def mine(i, j):
    if masu[i][j] == ".":
        masu[i][j] = 0
    if masu[i][j] != "#":
        masu[i][j] += 1
    return masu[i][j]


h, w = map(int, input().split())
masu = [[0]*(w+2) for _ in range(h+2)]

for i in range(1, h+1):
    masu[i] = [0]+list(input())+[0]
for i in range(h+2):
    for j in range(w+2):
        if masu[i][j] == ".":
            masu[i][j] = 0
        if masu[i][j] == "#":
            masu[i-1][j-1] = mine(i-1, j-1)
            masu[i-1][j] = mine(i-1, j)
            masu[i-1][j+1] = mine(i-1, j+1)
            masu[i][j-1] = mine(i, j-1)
            masu[i][j+1] = mine(i, j+1)
            masu[i+1][j-1] = mine(i+1, j-1)
            masu[i+1][j] = mine(i+1, j)
            masu[i+1][j+1] = mine(i+1, j+1)

for i in range(1, h+1):
    print("".join(map(str, masu[i][1:-1])))
