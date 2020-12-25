from functools import lru_cache

cost = 0

@lru_cache(maxsize=None)
def step(N, S, K):
    num = (N - S) // K
    if num == 0:
        return 0, num

    return S + K * (num+1) - N, num+1

def solve(N, S, K) -> int:
    memo = [0]*N
    now = S
    cost = 0
    while now != 0:
        now, cost = step(N, now, K)
        if memo[now] != 0:
            return -1

        memo[now] = 1
        cost += cost

    return cost


def main():
    T = int(input())
    tests = [list(map(int, input().split())) for _ in range(T)]
    for t in tests:
        print(solve(t[0], t[1], t[2]))

if __name__ == '__main__':
    main()
