from typing import Optional


def takahashi() -> bool:
    dp = {n: set() for n in range(N+1)}
    dp[N] = {0}

    for i in reversed(range(N)):
        next_set = dp[i+1]
        from0 = {r for r in range(7) if (10*r+int(S[i]))%7 in next_set}
        fromS = {r for r in range(7) if (10*r)%7 in next_set}
        if X[i] == "T":
            dp[i] = from0 | fromS
        elif X[i] == "A":
            dp[i] = from0 & fromS
        else:
            raise Exception(f"X: {X[i+1]}")

    return len(dp[0]) != 0

def solve() -> str:
    m = takahashi()
    if m:
        return "Takahashi"
    else:
        return "Aoki"


def main():
    global N, S, X

    N = int(input())
    S = input()
    X = input()

    ans = solve()
    print(ans)

if __name__ == '__main__':
    main()
