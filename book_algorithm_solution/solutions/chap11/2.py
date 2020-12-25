# input:
#   N M
#   idx
#   e1_left e1_right
#   e2_left e2_right
#   ...
#   em_left em_right
# output:
#   number of united clusters after deletion of edges whose index is less than or equal to given index

import numpy as np

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = np.zeros(N) - 1
        self.siz = np.zeros(N) + 1

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x

        self.par[x] = self.root(int(self.par[x]))
        return self.par[x]

    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x, y = self.root(x), self.root(y)
        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]

def solve(N, M, E, idx) -> int:
    LEFT = 0
    RIGHT = 1
    uf = UnionFind(N)
    for e in E[idx+1:]:
        uf.unite(e[LEFT], e[RIGHT])

    cnt = 0
    for vertex_idx in range(N):
        if uf.root(vertex_idx) == vertex_idx:
            cnt += 1

    return cnt

def main():
    N, M = map(int, input().split())
    idx = int(input())
    E = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    print(solve(N, M, E, idx))

if __name__ == "__main__":
    main()

