# https://qiita.com/drken/items/cce6fc5c579051e64fab
import numpy as np

YES = 'Yes'
NO = 'No'
import sys
if sys.version_info.minor >= 9:
    from typing import Literal
    YES_NO = Literal[YES, NO]
else:
    YES_NO = str

# Conditions
LEFT = 0
RIGHT = 1
DISTANCE = 2

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]
        self.rank = [0]*N
        self.weight_diff = [0]*N

    def root(self, x: int) -> int:
        if self.par[x] == x:
            return x

        root = self.root(self.par[x])
        self.weight_diff[x] += self.weight_diff[self.par[x]]
        self.par[x] = root
        return self.par[x]

    def weight(self, x: int) -> int:
        self.root(x)
        return self.weight_diff[x]

    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int, weight: int) -> bool:
        weight += self.weight(x) - self.weight(y)
        x, y = self.root(x), self.root(y)
        if x == y:
            return False

        if self.rank[x] < self.rank[y]:
            x, y = y, x
            weight = -weight
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

        self.par[y] = x
        self.weight_diff[y] += weight
        return True

    def diff(self, x: int, y: int) -> int:
        return self.weight(y) - self.weight(x)

def solve(N: int, M: int, conditions: list) -> YES_NO:
    uf = UnionFind(N)
    for c in conditions:
        if uf.issame(c[LEFT], c[RIGHT]):
            if uf.diff(c[LEFT], c[RIGHT]) != c[DISTANCE]:
                break
        else:
            uf.unite(c[LEFT], c[RIGHT], c[DISTANCE])
    else:
        return YES

    return NO

def main():
    N, M = map(int, input().split())
    conditions = [list(map(lambda e: int(e[1]) - 1 if e[0] in (LEFT, RIGHT) else int(e[1]), enumerate(input().split()))) for _ in range(M)]
    print(solve(N, M, conditions))

if __name__ == '__main__':
    main()
