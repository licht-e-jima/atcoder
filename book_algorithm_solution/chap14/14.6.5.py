from dataclasses import dataclass
from typing import Callable, List, Dict, Tuple, Optional, Union

# 無限大を表す値(ここでは 2^60 とする)
INF = 1 << 60


# 辺を表す型
@dataclass
class Edge:
    to: int
    w: int


# 重み付きグラフを表す型
@dataclass
class Graph:
    n: int

    def __post_init__(self):
        self.__dict: Dict[int, List[Edge]] = {i: [] for i in range(self.n)}

    def __getitem__(self, item: int):
        return self.__dict[item]

# 緩和を実施する関数
def chmin(a: int, b: int) -> Tuple[int, bool]:
    if a > b:
        return b, True
    else:
        return a, False

# ヒープ
class Heap:
    KEY: int = 0
    VERTEX: int = 1

    def __init__(
        self,
        compare: Callable[[int, int], bool] = lambda parent, child: parent >= child
    ):
        self.__heap: List[Tuple[int, int]] = []
        self.__compare = compare

    def push(self, tup: Tuple[int, int]) -> None:
        # 最後尾に挿入
        self.__heap.append(tup)
        # 挿入された頂点の番号
        i = len(self.__heap) - 1
        while i > 0:
            # 親の頂点番号
            p = (i - 1) // 2
            # 逆転がなければ終了
            if self.__compare(self.__heap[p][self.KEY], tup[self.KEY]):
                break

            # 自分の値を親の値にする
            self.__heap[i] = self.__heap[p]
            # 自分は上に行く
            i = p

        # tup は最終的にこの位置に持ってくる
        self.__heap[i] = tup

    # 最大値を取得する
    def top(self) -> Tuple[int, int]:
        assert self.__heap
        return self.__heap[0]

    # 最大値を削除
    def pop(self) -> None:
        if not self.__heap:
            return
        elif len(self.__heap) == 1:
            self.__heap.pop()
            return

        x: Tuple[int, int] = self.__heap[-1]
        self.__heap.pop(0)

        # 根から降ろしてくる
        i: int = 0
        while i * 2 + 1 < len(self.__heap):
            # 子頂点同士を比較, より親に近い値を child1 とする
            child1: int = i * 2 + 1
            child2: int = i * 2 + 2
            if child2 < len(self.__heap) \
            and self.__compare(self.__heap[child2][self.KEY], self.__heap[child1][self.KEY]):
                child1 = child2

            # 逆転がなければ終了
            if self.__compare(x[self.KEY], self.__heap[child1][self.KEY]):
                break
            # 自分の値を子頂点の値にする
            self.__heap[i] = self.__heap[child1]
            # 自分は下に行く
            i = child1

        # x は最終的にこの位置に持ってくる
        self.__heap[i] = x

    def empty(self) -> bool:
        return len(self.__heap) == 0



def main():
    # 頂点数, 辺数, 始点
    N, M, s = map(int, map(int, input().split()))

    # グラフ
    G = Graph(N)
    for _ in range(M):
        a, b, w = map(int, input().split())
        G[a].append(Edge(b, w))

    # ダイクストラ法
    dist: List[int] = [INF for _ in range(N)]
    dist[s] = 0

    # (d[v], v) のペアを要素としたヒープを作る
    que: Heap = Heap(compare=lambda parent, child: parent <= child)
    que.push((dist[s], s))

    # ダイクストラ法の反復を開始
    while not que.empty():
        # v: 使用済みでない頂点のうち d[v] が最小の頂点
        # d: v に対するキー値
        v: int = que.top()[1]
        d: int = que.top()[0]
        que.pop()

        # d > dist[v] は (d, v) がゴミであることを示す
        if d > dist[v]:
            continue

        # 頂点 v を始点とした各辺を緩和
        for e in G[v]:
            dist[e.to], reduction = chmin(dist[e.to], dist[v] + e.w)
            if reduction:
                # 更新があるならヒープに新たに挿入
                que.push((dist[e.to], e.to))

    # 結果出力
    for v in range(N):
        if dist[v] < INF:
            print(f"{v}: {dist[v]}")
        else:
            print(f"{v}: INF")



if __name__ == "__main__":
    main()

"""sample input
7 9 0
0 1 3
0 2 5
1 2 4
1 3 12
2 3 9
2 4 4
4 3 7
3 5 2
4 5 8
"""
