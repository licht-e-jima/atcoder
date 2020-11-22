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
