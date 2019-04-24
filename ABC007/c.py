r, c = map(int, input().split())
start = list(map(int, input().split()))
gole = list(map(int, input().split()))
maze = [[0]*c]*r
check = [[0]*c]*r


for y in range(r):
    maze[y] = list(input())

print(maze)
