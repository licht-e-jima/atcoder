
from typing import Dict

class UnionFind:
    par: Dict[int, int]
    siz: Dict[int, int]

    def __init__(self, N: int) -> None:
        self.par = {i: -1 for i in range(N)}
        self.siz = {i: 1 for i in range(N)}

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            y, x = x, y

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]

if __name__ == "__main__":
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for i in range(M):
        a, b = map(int, input().split())
        uf.unite(a, b)

    # 連結成分の個数を求める
    res = 0
    for x in range(N):
        if uf.root(x) == x:
            res += 1
    print(res)
