from collections import deque
from copy import deepcopy
from typing import *

class UnableToColor(BaseException):...

class Graph:
    def __init__(self, n: int, edges: List[List[int]]=None, nodes: Dict[int, Set[int]]=None):
        self.N = n
        if edges is not None:
            self.connected_nodes = {i: set() for i in range(1, n+1)}
            for e in edges:
                if len(self.connected_nodes[e[0]]) >= 2 or len(self.connected_nodes[e[1]]) >= 2:
                    raise UnableToColor()

                self.connected_nodes[e[0]].add(e[1])
                self.connected_nodes[e[1]].add(e[0])
        elif nodes is not None:
            self.connected_nodes = nodes
        else:
            raise Exception()

    def directly_connecteds(self, n):
        return self.connected_nodes[n]

    def get_connecteds(self, node):
        is_connecteds = {i: False for i in range(1, self.N+1)}
        is_connecteds[node] = True
        queue = deque()
        for _n in self.directly_connecteds(node):
            queue.append(_n)
        while len(queue) > 0:
            target = queue.pop()
            is_connecteds[target] = True
            for _n in self.directly_connecteds(target):
                if is_connecteds[_n]:
                    continue
                queue.append(_n)
        return [
            k
            for k, v in is_connecteds.items()
            if v
        ]

    def get_copy_from_nodes(self, nodes: List[int]) -> "Graph":
        nodes = deepcopy(nodes)
        nodes.sort()
        connected_nodes = {
            k: v
            for k, v in self.connected_nodes.items()
            if k in nodes
        }
        for i in range(len(nodes)):
            old = nodes[i]
            if old == i+1:
                continue

            nodes[i] = i+1
            old_nodes = connected_nodes.pop(old)
            for o in old_nodes:
                connected_nodes[o].discard(old)
                connected_nodes[o].add(i+1)
            connected_nodes[i+1] = old_nodes
        return Graph(len(nodes), None, connected_nodes)

    def remove_nodes(self, nodes: List[int]):
        for n in nodes:
            self.connected_nodes.pop(n)

    def degression(self) -> List['Graph']:
        graphs = []
        connecteds = self.get_connecteds(1)
        graphs.append(self.get_copy_from_nodes(connecteds))
        self.remove_nodes(connecteds)
        while len(self.connected_nodes) > 0:
            connecteds = self.get_connecteds(
                list(self.connected_nodes.keys())[0]  # 遅い
            )
            graphs.append(self.get_copy_from_nodes(connecteds))
            self.remove_nodes(connecteds)
        return graphs

class Map:
    def __init__(self, n: int):
        self.colors = {i: -1 for i in range(1, n+1)}
        self.n = n
        self.fixed = 0

    def next(self):
        self.fixed += 1
        return self.fixed

    def get_colors(self, nodes: Set[int]):
        colors = set()
        for n in nodes:
            if self.colors[n] == -1:
                continue

            colors.add(self.colors[n])
        return colors

    def coloring(self, node: int, color: int):
        self.colors[node] = color


def solve(N, M, edges):
    graph = Graph(N, edges)
    graphs = graph.degression()
    cnts = []
    for g in graphs:
        queue = deque()
        for i in range(3):
            mapping = Map(g.N)
            node = mapping.next()
            mapping.coloring(node, i)
            queue.append(mapping)
        cnt = 0
        while len(queue) > 0:
            current = queue.pop()
            node = current.next()
            if node == g.N+1:
                cnt += 1
                continue

            connected_nodes = g.directly_connecteds(node)
            colors = current.get_colors(connected_nodes)
            for i in range(3):
                if i not in colors:
                    new_map = deepcopy(current)
                    new_map.coloring(node, i)
                    queue.append(new_map)
        cnts.append(cnt)
    cnt = 1
    for c in cnts:
        cnt *= c
    return cnt

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(
            list(map(int, input().split()))
        )
    try:
        answer = solve(N, M, edges)
        print(answer)
    except UnableToColor:
        print(0)


if __name__ == '__main__':
    main()
