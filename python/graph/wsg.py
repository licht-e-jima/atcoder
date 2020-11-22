from random import random, choice
from typing import List, Tuple

from .graph import Graph, Node

class WSG(Graph):
    """Watts-Strogattz Model
    """

    def __init__(self, N: int, K: int, beta: float, print_edges: bool = False) -> None:
        """
        Args:
            N (int): Number of nodes
            K (int): mean degree of nodes will be 2 * K. K ∈ {R | 1 <= K < N / 2}
            beta (float): rewireing probability
            print_edges (bool): if print edges for debug
        """
        def edge(idx: int) -> Tuple[Node, Node]:
            node_idx = Node(idx // K)
            edge_idx = idx % K
            the_other_node_idx = Node((node_idx + edge_idx + 1) % N)
            return node_idx, the_other_node_idx

        edges = list(map(edge, range(N*K)))
        edges = self.__rewire1(edges, N, beta)
        if print_edges:
            print(edges)

        super().__init__(N, edges)

    def __rewire1(self, edges: List[Tuple[Node, Node]], N: int,  beta: float) -> List[Tuple[Node, Node]]:
        def pick_unconnected(node: Node, edges: List[Tuple[Node, Node]]) -> Node:
            unconnecteds = list(
                filter(
                    lambda n: n != node and all(e not in [(n, node), (node, n)] for e in edges),
                    range(N)
                )
            )
            return choice(unconnecteds)

        for idx, e in enumerate(edges):
            if random() <= beta:
                node = e[0]
                the_other = pick_unconnected(node, edges)
                edges[idx] = (node, the_other)

        return edges


    def __rewire2(self, edges: List[Tuple[Node, Node]], N: int, beta: float) -> List[Tuple[Node, Node]]:
        def duplicated(edge: Tuple[Node, Node], edges: List[Tuple[Node, Node]]) -> bool:
            node = edge[0]
            the_other = edge[1]
            for e in edges:
                if e[0] == node and e[1] == the_other:
                    return True
                elif e[0] == the_other and e[1] == node:
                    return True
            else:
                return False

        def rewire(node: Node, edges: List[Tuple[int, int]]) -> Tuple[int, int]:
            if random() < beta:
                while True:
                    the_other = choice(range(N))
                    if the_other != node and not duplicated((node, the_other), edges):
                        return the_other
            else:
                return e

        for idx, e in enumerate(edges):
            if random() <= beta:
                node = e[0]
                e = rewire(node, edges)
                edges[idx] = e

        return edges

if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    graph = WSG(40, 2, 0.2, True)
    print(graph.mean_distance())
    end = datetime.now()
    print(f'Total: {end - start}')
