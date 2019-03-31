h, w = map(int, input().split())
pict = [[0]*(w+2) for _ in range(h+2)]

for y in range(1, h+1):
    pict[y][1:w+1] = list(input())
ans = "Yes"
for y in range(h):
    for x in range(w):
        if pict[y][x] == "#":
            if pict[y-1][x] == "." and pict[y+1][x] == "." and pict[y][x-1] == "." and pict[y][x+1] == ".":
                ans = "No"
print(ans)
