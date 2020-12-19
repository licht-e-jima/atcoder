def query_1(N: int, A: list, x: int, y: int):
    A[x-1] = A[x-1] ^ y

def query_2(N: int, A: list, x: int, y: int) -> int:
    ans = A[x-1]
    for a in A[x:y]:
        ans = ans ^ a
    return ans

QUERY_1 = 1
QUERY_2 = 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    for T, X, Y in queries:
        if T == QUERY_1:
            query_1(N, A, X, Y)
        elif T == QUERY_2:
            print(query_2(N, A, X, Y))
        else:
            raise Exception(T)

if __name__ == '__main__':
    main()
