from random import random
from itertools import combinations

from .graph import Graph

class ERRG(Graph):
    """Erdös-Rényi Random Graph
    """

    def __init__(self, num_of_nodes: int, prob: float, print_edges: bool = False) -> None:
        edges = list(filter(
            lambda _: random() <= prob,
            combinations(range(num_of_nodes), 2)
        ))
        if print_edges:
            print(edges)
        super().__init__(num_of_nodes, edges)

if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    graph = ERRG(1000, 0.008, False)
    print(graph.is_connected())
    print(graph.clusters())
    end = datetime.now()
    print(f'Total: {end - start}')
