from typing import List

def count(X: int, line: List[str]) -> int:
    is_include = False
    count = 0
    for i, s in enumerate(line):
        if s == "#" and not is_include:
            count = 0
        elif s == "#" and is_include:
            return count
        elif s == "." and not is_include and i == X-1:
            count += 1
            is_include = True
        elif s == ".":
            count += 1
        else:
            raise Exception(f"unexpected: {i}, {s}")

    return count


def solve(H: int, W: int, X: int, Y: int, S: List[str]) -> int:
    Sy = [S[i][Y-1] for i in range(H)]
    Sx = list(S[X-1])
    return count(Y, Sx) + count(X, Sy) - 1

def main():
    H, W, X, Y = map(int, map(int, input().split()))
    S = [
        input()
        for _ in range(H)
    ]
    answer = solve(H, W, X, Y, S)
    print(answer)

if __name__ == '__main__':
    main()
