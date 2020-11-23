from dataclasses import dataclass
from itertools import combinations
from typing import List

WALL = '#'

@dataclass(frozen=True)
class Position:
    h: int
    w: int
    s: str

    def is_wall(self) -> bool:
        return self.s == WALL

@dataclass(frozen=True)
class Edge:
    p1: Position
    p2: Position

@dataclass(frozen=True)
class EdgeList:
    l: List[Edge]

    def add(self, edge: Edge) -> None:
        self.l.append(edge)

class Map:
    def __init__(self, H: int, W: int, a: List[List[str]]) -> None:
        self.H = H
        self.W = W
        self.a = a
        self.positions: List[List[Position]] = [[Position(h, w, a[h][w]) for w in range(W)] for h in range(H)]
        self.edges: EdgeList = EdgeList([])
        # a = 97 ~ z = 122
        for i in range(97, 123):
            positions = self.get_positions_by_str(chr(i))
            for combi in combinations(positions, 2):
                self.edges.add(Edge(combi[0], combi[1]))

        # 隣会う Position をエッジでつなぐ
        for h in range(H):
            for w in range(W):
                me = self.positions[h][w]
                if me.is_wall():
                    continue

                if h != H - 1:
                    below = self.positions[h+1][w]
                    if not below.is_wall():
                        self.edges.add(Edge(me, below))

                if w != W - 1:
                    right = self.positions[h][w+1]
                    if not right.is_wall():
                        self.edges.add(Edge(me, right))

        self.__connected_positions: List[List[List[Position]]] = [
            [
                list(map(
                    lambda e: e.p1 if e.p2 == self.positions[h][w] else e.p2,
                    filter(
                        lambda e: e.p1 == self.positions[h][w] or e.p2 == self.positions[h][w],
                        self.edges.l
                    )
                ))
                for w in range(W)
            ] for h in range(H)
        ]

    def get_positions_by_str(self, s: str) -> List[Position]:
        positions: List[Position] = []
        for row in self.positions:
            for pos in row:
                if pos.s == s:
                    positions.append(pos)

        return positions

    def start(self) -> Position:
        return self.get_positions_by_str('S')[0]

    def goal(self) -> Position:
        return self.get_positions_by_str('G')[0]

    def distance(self, start: Position, goal: Position) -> int:
        distances = [[None for w in range(self.W)] for h in range(self.H)]

        distance = 0
        queues = [start]
        # 幅優先探索
        while len(queues) > 0:
            self.print_map(queues)
            queue_length = len(queues)
            for i in range(queue_length):
                pos = queues[i]
                if pos == goal:
                    return distance

                if distances[pos.h][pos.w] is None:
                    distances[pos.h][pos.w] = distance
                else:
                    continue

                connecteds = self.__connected_positions[pos.h][pos.w]
                queues.extend(connecteds)
            queues = queues[queue_length:]
            distance += 1
        else:
            return -1

    def print_map(self, positions: List[Position]) -> None:
        print(''.join('-' for _ in range(self.W*2+7)))

        for h in range(self.H):
            ps = list(map(lambda p: p.w, filter(lambda p: p.h == h, positions)))
            row = ['X' if i in ps else '·' for i in range(self.W)]
            print('| ', end='')
            print(''.join(row), end='')
            print(' | ', end='')
            print(''.join(self.a[h]), end='')
            print(' |')

        print(''.join('-' for _ in range(self.W*2+7)))

def solve(H: int, W: int, a: List[List[str]]) -> int:
    map = Map(H, W, a)
    start = map.start()
    goal = map.goal()
    return map.distance(start, goal)

def main():
    # H, W = map(int, input().split())
    # a = [list(input()) for _ in range(H)]
    H, W = (11, 11)
    a = [
        list('.#.#.e#a...'),
        list('.b..##..#..'),
        list('#....#.#..#'),
        list('.#dd..#..#.'),
        list('....#...#e.'),
        list('c#.#a....#.'),
        list('.....#..#.e'),
        list('.#....#b.#.'),
        list('.#...#..#..'),
        list('......#c#G.'),
        list('#..S...#...'),
    ]

    print(solve(H, W, a))

if __name__ == '__main__':
    main()
