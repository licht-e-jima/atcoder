from typing import List

def check(P: List[int]) -> bool:
    return all(
        map(
            lambda t: P[t[0]] + 1 == t[1],
            enumerate(P[1:])
        )
    )

def recursive(N: int, P: List[int], minimum: int) -> List[int]:
    if N == 0:
        return []
    elif N == 1:
        return []
    elif N == 2:
        if P[0] == minimum+1 and P[1] == minimum:
            return [minimum]
        else:
            return [-1]

    min_idx = P.index(minimum)
    Q = P[:min_idx-1]
    if not check(Q):
        return [-1]

    orders = [i for i in reversed(range(minimum, minimum+min_idx))]
    next_N = len(P[min_idx:])
    next_P = [P[min_idx-1]]
    next_P.extend(P[min_idx+1:])
    next_minimum = min(next_P)
    next_orders = recursive(next_N, next_P, next_minimum)
    if next_orders == [-1]:
        return [-1]
    else:
        orders.extend(next_orders)
        return orders


def solve(N: int, P: List[int]) -> List[int]:
    minimum = min(P)
    return recursive(N, P, minimum)

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = solve(N, P)
    print('\n'.join(str(i) for i in ans))

if __name__ == '__main__':
    main()
