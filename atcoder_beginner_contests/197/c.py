from functools import lru_cache
from typing import List, Tuple, Generator

def get(A: List[int]) -> Generator[int, None, None]:
    for i in range(1, len(A)+1):
        or_list = A[:i]
        or_num = 0
        for j in or_list:
            or_num = or_num | j
        if len(A[i:]) == 0:
            yield or_num
        else:
            for o in get(A[i:]):
                yield or_num ^ o

INF = 1 << 40

def solve(N: int, A: List[int]) -> int:
    answer = INF
    for i in get(A):
        answer = min(i, answer)
    return answer

def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = solve(N, A)
    print(answer)

if __name__ == '__main__':
    main()
