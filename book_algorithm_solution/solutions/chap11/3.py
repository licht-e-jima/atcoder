# input:
#   N K L
#   idx
#   road1_left road1_right
#   road2_left road2_right
#   ...
#   roadk_left roadk_right
#   railway1_left railway1_right
#   railway2_left railway2_right
#   ...
#   railwayl_left railwayl_right
# output:
#   number of cities which can be reached by using only roads and can be reached by using only railways from the city with given index

import numpy as np

class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = np.zeros(N) - 1
        self.siz = np.zeros(N) + 1

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x

        return self.root(int(self.par[x]))

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

def solve(N, K, L, idx, Roads, Railways) -> int:
    LEFT = 0
    RIGHT = 1

    uf_road = UnionFind(N)
    for e in Roads:
        uf_road.unite(e[LEFT], e[RIGHT])

    uf_railway = UnionFind(N)
    for e in Railways:
        uf_railway.unite(e[LEFT], e[RIGHT])

    cnt = 0
    for i in range(N):
        if i == idx:
            continue
        elif uf_road.issame(idx, i) and uf_railway.issame(idx, i):
            cnt += 1
    return cnt

def main():
    N, K, L = map(int, input().split())
    idx = int(input())
    Roads = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
    Railways = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(L)]
    print(solve(N, K, L, idx, Roads, Railways))

if __name__ == "__main__":
    main()

