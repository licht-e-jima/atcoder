from typing import List, Tuple
from functools import lru_cache


def get_remain(boxes: List[int], L: int, R: int) -> List[int]:
    return boxes[:L-1] + boxes[R:]


def solve(
    N: int,
    M: int,
    buggages: List[Tuple[int,int]],
    boxes: List[int],
    q: Tuple[int,int]
):
    buggages.sort(key=lambda b: b[1], reverse=True)
    available: List[Tuple[int,int]] = list(buggages)

    remain = get_remain(boxes, q[0], q[1])
    remain.sort()

    value = 0
    for buggage in available:
        for i, box in enumerate(remain):
            if buggage[0] > box:
                continue

            value += buggage[1]
            remain = remain[:i] + remain[i+1:]
            break

    return value


def main():
    N, M, Q = map(int, input().split())
    buggages = [
        tuple(map(int, input().split()))
        for _ in range(N)
    ]
    boxes = list(map(int, input().split()))
    queries = [
        tuple(map(int, input().split()))
        for _ in range(Q)
    ]
    for q in queries:
        ans = solve(N, M, buggages, boxes, q)
        print(ans)

if __name__ == '__main__':
    main()
