from collections import deque
from dataclasses import dataclass
import itertools
import sys
from typing import List

def flatten(l_2d: List[list]) -> list:
    return list(itertools.chain.from_iterable(l_2d))

@dataclass(frozen=True)
class Query:
    h_index: int
    w_index: int
    t_index: int
    turned: bool

    @property
    def is_rightmost(self) -> bool:
        return self.w_index == max_w_index

    @property
    def is_bottom(self) -> bool:
        return self.h_index == max_h_index

    @property
    def is_fulfilled(self) -> bool:
        return self.t_index == max_t_index

    def right(self) -> 'Query':
        return Query(
            self.h_index,
            self.w_index + 1,
            self.t_index + 1,
            False,
        )

    def down(self) -> 'Query':
        return Query(
            self.h_index + 1,
            self.w_index,
            self.t_index + 1,
            True,
        )

def solve(
    H: int,  # 高さ
    W: int,  # 幅
    S: List[str],  # 盤面
    T: str,  # 一致させる文字列
) -> int:
    global max_h_index, max_w_index, max_t_index
    max_h_index = H - 1
    max_w_index = W - 1
    max_t_index = len(T) - 1

    queue = deque(flatten(
        [
            [
                Query(h, w, 0, False)
                for w, s in enumerate(l)
                if s == T[0]
            ]
            for h, l in enumerate(S)
        ]
    ))

    cnt = 0
    while True:
        if len(queue) == 0:
            break

        now = queue.pop()
        if now.is_fulfilled:
            cnt += 1
            continue

        next_t = T[now.t_index+1]
        # 下に移動
        if not now.is_bottom:
            able_to_go_down = S[now.h_index+1][now.w_index] == next_t
            if able_to_go_down:
                queue.append(now.down())

        # 右に移動
        if not now.turned and not now.is_rightmost:
            able_to_go_right = S[now.h_index][now.w_index+1] == next_t
            if able_to_go_right:
                queue.append(now.right())

    return cnt
