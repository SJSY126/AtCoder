class UnionFind():
    __slots__ = ['parent']
    # 負の値はルートで集合の個数
    # 正の値は次の要素を返す

    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.parent[parent_x] < self.parent[parent_y]:
                self.parent[parent_x] += self.parent[parent_y]
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_y] += self.parent[parent_x]
                self.parent[parent_x] = parent_y

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        while self.parent[x] >= 0:
            x = self.find(self.parent[x])
        return abs(self.parent[x])


n, m = map(int, input().split())

brige = [list(map(int, input().split())) for _ in range(m)]

uf = UnionFind(n)
ans = [0] * m
ans[m-1] = int(n*(n-1)/2)

for i in range(m-1, 0, -1):
    a = brige[i][0]-1
    b = brige[i][1]-1
    if uf.find(a) != uf.find(b):
        ans[i-1] = ans[i] - uf.size(a)*uf.size(b)
    else:
        ans[i-1] = ans[i]
    uf.union(a, b)

for ans_i in ans:
    print(int(ans_i))
