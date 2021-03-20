from collections import deque
from copy import deepcopy
from dataclasses import dataclass


class Row:
    W: int = 0

    def __init__(self):
        self.row = [0]*self.W

    def put(self, idx: int):
        self.row[idx] = 1

    def is_filled(self, idx: int):
        return self.row[idx] == 1


@dataclass(frozen=True)
class State:
    h: int
    w: int
    current: Row
    bellow: Row
    A: int
    B: int


class Map:
    def __init__(self, H: int, W: int, A: int, B: int):
        self.H = H
        self.W = W
        Row.W = W

        self.A = A
        self.B = B

    def solve(self):
        cnt = 0
        queue = deque()
        state = State(0, 0, Row(), Row(), self.A, self.B)
        queue.append(state)

        while len(queue) != 0:
            state: State = queue.pop()
            # print('=======')
            # print(f"h: {state.h}, w: {state.w}, A: {state.A}, B: {state.B}")
            # print(f"current: {''.join(list(map(str,state.current.row)))}")
            # print(f" bellow: {''.join(list(map(str,state.bellow.row)))}")
            if state.h == self.H-1 and state.w == self.W:
                cnt += 1
                continue

            if state.w == self.W:
                h = state.h + 1
                w = 0
                current = state.bellow
                bellow = Row()
            else:
                h = state.h
                w = state.w
                current = state.current
                bellow = state.bellow

            if current.is_filled(w):
                new_state = State(
                    h,
                    w+1,
                    current,
                    bellow,
                    state.A,
                    state.B,
                )
                queue.append(new_state)
                continue

            if state.A != 0:
                # 縦におく
                if h != self.H-1 and not bellow.is_filled(w):
                    new_current = deepcopy(current)
                    new_bellow = deepcopy(bellow)

                    new_current.put(w)
                    new_bellow.put(w)

                    new_state = State(
                        h,
                        w+1,
                        new_current,
                        new_bellow,
                        state.A-1,
                        state.B,
                    )
                    queue.append(new_state)

                # 横におく
                if w != self.W-1 and not current.is_filled(w+1):
                    new_current = deepcopy(current)
                    new_bellow = deepcopy(bellow)

                    new_current.put(w)
                    new_current.put(w+1)

                    new_state = State(
                        h,
                        w+1,
                        new_current,
                        new_bellow,
                        state.A-1,
                        state.B,
                    )
                    queue.append(new_state)

            if state.B != 0:
                new_current = deepcopy(current)
                new_bellow = deepcopy(bellow)

                new_current.put(w)

                new_state = State(
                    h,
                    w+1,
                    new_current,
                    new_bellow,
                    state.A,
                    state.B-1,
                )
                queue.append(new_state)
        return cnt


def solve(
    H: int,
    W: int,
    A: int,
    B: int,
):
    m = Map(H, W, A, B)
    return m.solve()


def main():
    H, W, A, B = map(int, input().split())
    ans = solve(H, W, A, B)
    print(ans)


if __name__ == '__main__':
    main()
