def search(x, y):
    if maze[y][x] == ".":
        return True


r, c = map(int, input().split())
start = list(map(int, input().split()))
gole = list(map(int, input().split()))
maze = [[0]*c]*r

queue = []

for y in range(r):
    maze[y] = list(input())

cost = maze[:][:]
cost[start[0]-1][start[1]-1] = 0


queue.append([start[1]-1, start[0]-1])

while 1:
    now = queue.pop(0)
    x = now[0]
    y = now[1]

    if search(x+1, y):
        queue.append([x+1, y])
        cost[y][x+1] = 1 + cost[y][x]
    if search(x-1, y):
        queue.append([x-1, y])
        cost[y][x-1] = 1 + cost[y][x]
    if search(x, y+1):
        queue.append([x, y+1])
        cost[y+1][x] = 1 + cost[y][x]
    if search(x, y-1):
        queue.append([x, y-1])
        cost[y-1][x] = 1 + cost[y][x]
    if queue == []:
        break

print(cost[gole[0]-1][gole[1]-1])
