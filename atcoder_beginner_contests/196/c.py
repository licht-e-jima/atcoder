def even(N: int) -> int:
    N_str = str(N)
    N_len = len(N_str)
    half = N_len // 2

    left_str = N_str[:half]
    left_no = int(left_str)

    right_str = N_str[half:]
    right_no = int(right_str)

    if left_no > right_no:
        return left_no - 1
    else:
        return left_no

def solve(N: int) -> int:
    N_str = str(N)
    if len(N_str) % 2 == 0:
        return even(N)
    elif len(N_str) == 1:
        return 0
    else:
        N = N - int(N_str[1:]) - 1
        return solve(N)


def main():
    N = int(input())
    answer = solve(N)
    print(answer)


if __name__ == '__main__':
    main()
    # for i in range(100000):
    #     ans = solve(i)
    #     print(f"n: {i}\tans: {ans}")
