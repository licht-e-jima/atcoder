def solve(N, M, A):
    if len(A) == 0:
        return 1

    A.sort()
    whites = []
    for i, a in enumerate(A):
        if i == 0:
            if a != 1:
                whites.append(a-1)

            continue

        if A[i-1] + 1 == a:
            continue
        else:
            whites.append(a - A[i-1] - 1)
    else:
        if A[-1] != N:
            whites.append(N-A[-1])

    if len(whites) == 0:
        return 0

    k = min(whites)
    stumps = 0
    for w in whites:
        stumps += -(-w//k)

    return stumps


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))

if __name__ == '__main__':
    main()
