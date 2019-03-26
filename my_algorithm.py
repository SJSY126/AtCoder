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


class MemoFibo():
    def memo_fibo(n):
        memo = [0] * (n+1)

        def _fibo(n):
            if n == 1:
                return 0
            elif n == 2:
                memo[2] = 1
                return 1
            else:
                if memo[n] != 0:
                    return memo[n]
                memo[n] = (_fibo(n-1) + _fibo(n-2))
                return memo[n]

        return _fibo(n)
