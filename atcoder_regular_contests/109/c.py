from functools import lru_cache


def hand(i: int, n: int, s: str) -> str:
    hand_idx = i % n
    return s[hand_idx]

# ROCK_INT = 0
# SISSORS_INT = 1
# PAPER_INT = 2
# def rsp_with_int(a: int, b: int) -> int:
#     if (a - b) % 3 == 1:
#         return b
#     else:
#         return a

ROCK = 'R'
SISSORS = 'S'
PAPER = 'P'
def rsp(a: str, b: str) -> str:
    if a == b:
        return a
    elif a == ROCK and b == SISSORS:
        return ROCK
    elif a == ROCK and b == PAPER:
        return PAPER
    elif a == SISSORS and b == ROCK:
        return ROCK
    elif a == SISSORS and b == PAPER:
        return SISSORS
    elif a == PAPER and b == ROCK:
        return PAPER
    elif a == PAPER and b == SISSORS:
        return SISSORS
    else:
        raise Exception(f'a: {a}, b: {b}')

@lru_cache(maxsize=None)
def contest(l: int, participants: int, n: int, s: str) -> str:
    if participants == 1:
        return hand(l, n, s)
    else:
        half = participants // 2
        m = (l + half) % n
        l_hand = contest(l, half, n, s)
        r_hand = contest(m, half, n, s)
        return rsp(l_hand, r_hand)

def solve(n: int, k: int, s: str) -> str:
    l = 0
    r = 2 ** k
    length = r - l
    using = s if n <= r else s[:r]
    if ROCK * n == using:
        return ROCK
    elif SISSORS * n == using:
        return SISSORS
    elif PAPER * n == using:
        return PAPER
    elif ROCK not in using:
        return SISSORS
    elif SISSORS not in using:
        return PAPER
    elif PAPER not in using:
        return ROCK

    return contest(l, length, n, s)

def main():
    n, k = map(int, input().split())
    s = input()

    print(solve(n, k, s))

if __name__ == '__main__':
    main()
