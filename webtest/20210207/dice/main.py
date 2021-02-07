from typing import Dict, List, Set, Tuple

TOP, NORTH, SOUTH, WEST, EAST, BOTTOM = 0, 1, 2, 3, 4, 5

STATES = (
    (1, 5, 2, 3, 4, 6),
    (1, 3, 4, 2, 5, 6),
    (1, 2, 5, 4, 3, 6),
    (1, 4, 3, 5, 2, 6),
    (2, 1, 6, 3, 4, 5),
    (2, 3, 4, 6, 1, 5),
    (2, 6, 1, 4, 3, 5),
    (2, 4, 3, 1, 6, 5),
    (3, 5, 2, 6, 1, 4),
    (3, 6, 1, 2, 5, 4),
    (3, 2, 5, 1, 6, 4),
    (3, 1, 6, 5, 2, 4),
    (4, 5, 2, 1, 6, 3),
    (4, 1, 6, 2, 5, 3),
    (4, 2, 5, 6, 1, 3),
    (4, 6, 1, 5, 2, 3),
    (5, 6, 1, 3, 4, 2),
    (5, 3, 4, 1, 6, 2),
    (5, 1, 6, 4, 3, 2),
    (5, 4, 3, 6, 1, 2),
    (6, 2, 5, 3, 4, 1),
    (6, 3, 4, 5, 2, 1),
    (6, 5, 2, 4, 3, 1),
    (6, 4, 3, 2, 5, 1),
)

STATES_TO_IDX: Dict[Tuple[int,int,int,int,int,int],int] = {
    (1, 5, 2, 3, 4, 6): 0,
    (1, 3, 4, 2, 5, 6): 1,
    (1, 2, 5, 4, 3, 6): 2,
    (1, 4, 3, 5, 2, 6): 3,
    (2, 1, 6, 3, 4, 5): 4,
    (2, 3, 4, 6, 1, 5): 5,
    (2, 6, 1, 4, 3, 5): 6,
    (2, 4, 3, 1, 6, 5): 7,
    (3, 5, 2, 6, 1, 4): 8,
    (3, 6, 1, 2, 5, 4): 9,
    (3, 2, 5, 1, 6, 4): 10,
    (3, 1, 6, 5, 2, 4): 11,
    (4, 5, 2, 1, 6, 3): 12,
    (4, 1, 6, 2, 5, 3): 13,
    (4, 2, 5, 6, 1, 3): 14,
    (4, 6, 1, 5, 2, 3): 15,
    (5, 6, 1, 3, 4, 2): 16,
    (5, 3, 4, 1, 6, 2): 17,
    (5, 1, 6, 4, 3, 2): 18,
    (5, 4, 3, 6, 1, 2): 19,
    (6, 2, 5, 3, 4, 1): 20,
    (6, 3, 4, 5, 2, 1): 21,
    (6, 5, 2, 4, 3, 1): 22,
    (6, 4, 3, 2, 5, 1): 23,
}

class Map:
    def __init__(self, n, m, conditions):
        self.n = n
        self.m = m

        self.map: List[List[List]] = [[[] for _ in range(m)] for _ in range(n)]
        self.goal = (n-1, m-1)
        for c in conditions:
            self.map[c[0]][c[1]].append(c[2])

        self.visited: Set[Tuple[Tuple[int,int],int]] = set()  # set of i,j,state

    def bfs(self):
        queue: List[Tuple[Tuple[int,int],int]] = [((0,0),0)]  # list of i,j,state
        step = 0
        while len(queue) > 0:
            queue_len = len(queue)
            for i in range(queue_len):
                cur = queue[i]
                if cur[0] == self.goal:
                    return step

                self.visited.add(cur)
                queue.extend(self.next_states(*cur))

            queue = queue[queue_len:]
            step += 1
        else:
            return -1

    def next_states(self, cordinate, state):
        t, n, s, w, e, b = STATES[state]
        states: List[Tuple[Tuple[int, int], int]] = []
        i, j = cordinate
        if j > 0 and e not in self.map[i][j-1]:  # to west
            idx = STATES_TO_IDX[(e,n,s,t,b,w)]
            next_state = ((i,j-1),idx)
            if next_state not in self.visited:
                states.append(next_state)
        if j < self.m-1 and w not in self.map[i][j+1]:  # to east
            idx = STATES_TO_IDX[(w,n,s,b,t,e)]
            next_state = ((i,j+1),idx)
            if next_state not in self.visited:
                states.append(next_state)
        if i > 0 and s not in self.map[i-1][j]:  # to north
            idx = STATES_TO_IDX[(s,t,b,w,e,n)]
            next_state = ((i-1,j),idx)
            if next_state not in self.visited:
                states.append(next_state)
        if i < self.n-1 and n not in self.map[i+1][j]:  # to south
            idx = STATES_TO_IDX[(n,b,t,w,e,s)]
            next_state = ((i+1,j),idx)
            if next_state not in self.visited:
                states.append(next_state)

        return states


def main(lines):
    n, m, q, conditions = parse(lines)

    m = Map(n, m, conditions)
    step = m.bfs()
    if step >= 0:
        print("YES")
        print(step)
    else:
        print("NO")

def parse(lines):
    n, m, q = map(int, lines[0].split())
    conditions = list(map(
        lambda l: list(map(int, l.split())),
        lines[1:]
    ))
    return n, m, q, conditions

if __name__ == '__main__':
    lines = [
        "1 14 6",
        "0 6 4",
        "0 7 3",
        "0 2 1",
        "0 11 1",
        "0 5 1",
        "0 3 1",
    ]
    main(lines)
