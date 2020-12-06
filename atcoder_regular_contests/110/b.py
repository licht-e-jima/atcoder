REP = 10**10
S_LEN = 3*REP

def must_be_rep(N: int, T: str) -> bool:
    if N == 1:
        return T == '1'
    elif N == 2:
        return T == '11'

    for i in range(N//3):
        if not T[i*3:i*3+3] == '110':
            return False

    r = N % 3
    if r == 0:
        return True
    elif r == 1:
        return T[-1] == '1'
    elif r == 2:
        return T[-2:] == '11'

def solve(N: int, T: str) -> int:
    if N == 1:
        if T[0] == '1':
            return 2 * REP
        elif T[0] == '0':
            return REP
        else:
            return 0
    elif N == 2:
        if T[0] == '0' and T[1] == '1':
            return REP - 1
        elif T[0] == '1':
            return REP
        else:
            return 0

    start = 0
    if T[0] == '1':
        if T[1] == '0':
            start = 2
            if not must_be_rep(N-2, T[2:]):
                return 0
        elif T[1] == '1':
            if not must_be_rep(N, T):
                return 0
        else:
            return 0
    elif T[0] == '0':
        start = 1
        if not must_be_rep(N-1, T[1:]):
            return 0
    else:
        return 0

    reps = -(-(N-start) // 3)
    if start > 0:
        reps += 1

    return REP - reps + 1

def main():
    N = int(input())
    T = input()
    print(solve(N, T))

if __name__ == '__main__':
    main()
