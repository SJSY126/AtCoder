class UnionFind():
    __slot__ = ['parent']
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


n, q = map(int, input().split())

query = [list(map(int, input().split())) for _ in range(q)]
uf = UnionFind(n)


for i in range(q):
    if query[i][0] == 0:
        uf.union(query[i][1], query[i][2])
    else:
        if uf.is_same(query[i][1], query[i][2]):
            print("Yes")
        else:
            print("No")
