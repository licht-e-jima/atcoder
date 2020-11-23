from typing import List, Set, NewType, Tuple

WALL = '#'
START = 'S'
GOAL = 'G'

Y, X, CHAR = 0, 1, 2
position = NewType('Position', Tuple[int, int, str])

class Map:
    _A = 97
    _Z = 122
    _TELEPORTS: Set[str] = {chr(i) for i in range(_A, _Z+1)}

    def __init__(self, H: int, W: int, a: List[List[str]], debug=False) -> None:
        self.H = H
        self.W = W
        self.a = a
        self.debug = debug

        above, below, left, right = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        connection = [above, below, left, right]
        self.__teleports = {c: [] for c in self._TELEPORTS}
        def process(h, w, char) -> List[position]:
            if char in self._TELEPORTS:
                self.__teleports[char].append(position((h, w, char)))

            return [
                    position((h+c[Y], w+c[X], a[h+c[Y]][w+c[X]]))
                    for c in connection
                    if (h != 0 or c != above) and \
                        (h != H-1 or c != below) and \
                        (w != 0 or c != left) and \
                        (w != W-1 or c != right) and \
                        char != WALL and \
                        a[h+c[Y]][w+c[X]] != WALL
            ]

        self.__connected_positions: List[List[List[position]]] = [
            [
                process(h, w, char)
                for w, char in enumerate(row)
            ] for h, row in enumerate(a)
        ]

    def start(self) -> position:
        for h in range(self.H):
            for w in range(self.W):
                if self.a[h][w] == START:
                    return position((h, w, START))

    def goal(self) -> position:
        for h in range(self.H):
            for w in range(self.W):
                if self.a[h][w] == GOAL:
                    return position((h, w, GOAL))

    def distance(self, start: position, goal: position) -> int:
        distance = 0
        queues = [start]
        visited = set()
        # 幅優先探索
        while len(queues) > 0:
            if self.debug:
                self.print_map(queues)

            queue_length = len(queues)
            for i in range(queue_length):
                pos = queues[i]
                if pos == goal:
                    return distance

                visited.add(pos)
                connecteds = self.__connected_positions[pos[Y]][pos[X]]
                queues.extend(connecteds)
                if pos[CHAR] in self._TELEPORTS:
                    teleports = self.__teleports[pos[CHAR]]
                    queues.extend(teleports)

            queues = [q for q in queues[queue_length:] if q not in visited]
            distance += 1
        else:
            return -1

    def print_map(self, positions: List[position]) -> None:
        print(''.join('-' for _ in range(self.W*2+7)))

        for h in range(self.H):
            ps = list(map(lambda p: p[X], filter(lambda p: p[Y] == h, positions)))
            row = ['X' if i in ps else '·' for i in range(self.W)]
            print('| ', end='')
            print(''.join(row), end='')
            print(' | ', end='')
            print(''.join(self.a[h]), end='')
            print(' |')

        print(''.join('-' for _ in range(self.W*2+7)))

def solve(H: int, W: int, a: List[List[str]], debug=False) -> int:
    map = Map(H, W, a, debug)
    start = map.start()
    goal = map.goal()
    return map.distance(start, goal)

ss = """Sa...............................#...#...#...#....
#############......a.a..b..#...#z..#...#...#......
a........#..#...#...#...#....##...#...#.b.#....G.#"""

def test():
    a = list(map(lambda row: list(row), ss.split('\n')))
    H = len(a)
    W = len(a[0])

    print(solve(H, W, a, debug=True))

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]

    print(solve(H, W, a))

if __name__ == '__main__':
    test()
    # main()

