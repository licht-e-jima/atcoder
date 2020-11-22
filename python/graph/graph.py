from itertools import combinations
from typing import List, Tuple, NewType

Node = NewType('Node', int)

class Graph:

    def __init__(self, num_of_nodes: int, edges: List[Tuple[Node, Node]]):
        self.N = num_of_nodes
        self._connected_nodes = [list(
            map(
                lambda e: e[0] if e[1] == n else e[1],
                filter(
                    lambda e: e[0] == n or e[1] == n,
                    edges
                )
            )
        ) for n in range(self.N)]
        self._distances = None

    def is_connected(self) -> bool:
        checked = [False for _ in range(self.N)]
        def check(node: Node):
            checked[node] = True
            nodes = self._connected_nodes[node]
            for n in nodes:
                if checked[n]:
                    continue

                check(n)

        first_node = Node(0)
        check(first_node)
        return all(checked)

    def clusters(self) -> List[List[Node]]:
        checked = [False for _ in range(self.N)]
        def cluster(node: Node) -> List[Node]:
            cl = [node]
            checked[node] = True
            nodes = self._connected_nodes[node]
            for n in nodes:
                if checked[n]:
                    continue

                cl.extend(cluster(n))
            return cl

        clusters = []
        for n in range(self.N):
            if checked[n]:
                continue

            clusters.append(cluster(n))
        return clusters

    def mean_degree(self) -> float:
        return sum(map(lambda nodes: len(nodes), self._connected_nodes)) / self.N

    def distance(self, node: Node, the_other: Node) -> int:
        if self._distances is None:
            self._distances = [[None for _ in range(self.N)] for _ in range(self.N)]

        if self._distances[node][the_other] is not None:
            return self._distances[node][the_other]

        distance = 0
        nodes = [node]
        visiteds = []
        # 幅優先探索
        while distance < self.N:
            # すでに全てが計算済みのところに到達した場合はそれを返す
            # TODO: 全部が計算済みではなくても一部の計算を省くことができるはずなのでそこも改善できそう
            if all(self._distances[n][the_other] is not None for n in nodes):
                min_distance = min(self._distances[n][the_other] for n in nodes)
                distance += min_distance
                self._distances[node][the_other] = distance
                self._distances[the_other][node] = distance
                return distance

            for n_idx in range(len(nodes)):
                # キャッシュ
                if self._distances[node][nodes[n_idx]] is None:
                    self._distances[node][nodes[n_idx]] = distance
                    self._distances[nodes[n_idx]][node] = distance

                if nodes[n_idx] == the_other:
                    return distance

                # ループしてたらそれを除いて探索する
                visiteds.append(nodes[n_idx])
                connecteds = self._connected_nodes[nodes[n_idx]]
                nodes.extend(filter(lambda c: c not in visiteds, connecteds))

            distance += 1
        else:
            raise Exception('Nodes are not connected')

    def mean_distance(self) -> float:
        if not self.is_connected():
            raise Exception('Not fully connected. Cannot calculate mean distance')

        distances = 0
        num_of_combinations = self.N * (self.N - 1) * 0.5
        for combi in combinations(range(self.N), 2):
            distances += self.distance(*combi)

        return float(distances) / num_of_combinations

if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    graph = Graph(
        5,
        [(1,2), (0,1), (0,1), (0,0), (3,4)],
    )
    print(graph.is_connected())
    print(graph.clusters())
    end = datetime.now()
    print(f'Total: {end - start}')
