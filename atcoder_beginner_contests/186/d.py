from itertools import combinations

def solve(N, A):
    A.sort()
    minus = [(N-i-1)*a for i, a in enumerate(A[:-1])]
    plus = [(i+1)*a for i, a in enumerate(A[1:])]
    ans = sum(plus)
    ans -= sum(minus)
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


if __name__ == '__main__':
    main()
