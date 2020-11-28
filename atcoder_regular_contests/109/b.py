from math import floor, sqrt

def solve_with_confirmation(n: int, uncirtain_divided_woods: int) -> int:
    length = uncirtain_divided_woods * (uncirtain_divided_woods + 1) // 2
    if length > n + 1:
        divided_woods = uncirtain_divided_woods - 1
        return n - divided_woods + 1
    else:
        divided_woods = uncirtain_divided_woods
        return n - divided_woods + 1

def solve(n: int) -> int:
    solution = sqrt(2.25 + 2 * n) - 0.5
    divided_woods = floor(solution)
    if solution - divided_woods < 1e-10:
        return solve_with_confirmation(n, divided_woods)

    return n - divided_woods + 1

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()
