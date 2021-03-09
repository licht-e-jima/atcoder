from dataclasses import dataclass
from typing import Dict, List, Tuple, Set


INF = 1 << 30

@dataclass
class Edge:
    From: int
    To: int
    Rev: int
    Cap: int


class Graph:
    edges: Dict[int, List[Edge]]
    debug: bool = True

    def __init__(self, N: int, E: int, Edges: List[Tuple[int,int]]):
        self.node_num = N*2
        self.edge_num = E * 2 + N
        self.__reset_seen()

        self.edges = {n: [] for n in range(N*2)}

        self.__debug('============================================================')
        for n in range(N):
            cap = 1 if n != 0 else INF  # スタートノードは削除できないようにする
            self.__add_edge(n, n+N, cap)

        self.__debug('============================================================')
        for e in Edges:
            self.__add_edge(e[0]+N, e[1])
            self.__add_edge(e[1]+N, e[0])

    def __debug(self, s: str):
        if self.debug:
            print(s)

    def __add_edge(self, From: int, To: int, Cap: int = 1):
        fromrev = len(self.edges[From])
        torev = len(self.edges[To])
        self.__debug(f"From: {From}\tTo: {To}")
        self.edges[From].append(Edge(From, To, torev, Cap))
        self.edges[To].append(Edge(To, From, fromrev, 0))

    def __redge(self, edge: Edge) -> Edge:
        return self.edges[edge.To][edge.Rev]

    def __reset_seen(self):
        self.seen = {n: False for n in range(self.node_num)}

    def ford_fulkerson(self, S: int, P: Set[int]) -> int:
        res = 0
        self.__debug('============================================================')
        self.__debug(f"S: {S}")
        self.__debug(f"P: {P}")
        while True:
            self.__reset_seen()
            flow = self.__get_path(S, P, INF)
            if flow == 0:
                break

            res += flow

        return res

    def __get_path(self, S: int, P: Set[int], flow: int) -> int:
        """find a path by DFS"""
        if S in P:
            self.__debug(f"Reached: {S}")
            return flow

        self.seen[S] = True
        self.__debug(f"searching from: {S}")
        for e in self.edges[S]:
            self.__debug(f"\tTo: {e.To}\tCap: {e.Cap}\tFlow: {flow}")
            if self.seen[e.To] or e.Cap == 0:
                continue

            res = self.__get_path(e.To, P, min(flow, e.Cap))
            if res == 0:
                continue

            self.__run_flow(e, res)

            return res

        self.__debug(f"Path not found. From: {S}")
        return 0


    def __run_flow(self, edge: Edge, flow: int):
        edge.Cap -= flow
        self.__redge(edge).Cap += flow


def solve(N: int, G: int, E: int, P: List[int], Edges: List[Tuple[int,int]]) -> int:
    graph = Graph(N, E, Edges)
    return graph.ford_fulkerson(0, {p+N for p in P})

def main():
    N, G, E = map(int, input().split())
    P: List[int] = list(map(int, input().split()))
    Edges: List[Tuple[int,int]] = [
        tuple(map(int, input().split()))
        for _ in range(E)
    ]
    result = solve(N, G, E, P, Edges)
    print(result)


if __name__ == '__main__':
    main()
