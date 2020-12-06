def solve(N: int) -> int:
    x = 1
    for i in range(2, N + 1):
        if i == 6:
            continue
        elif i == 8:
            continue
        elif i == 10:
            continue
        elif i == 12:
            continue
        elif i == 14:
            continue
        elif i == 15:
            continue
        elif i == 16:
            x *= 2
            continue
        elif i == 18:
            continue
        elif i == 20:
            continue
        elif i == 21:
            continue
        elif i == 22:
            continue
        elif i == 24:
            continue
        elif i == 25:
            x *= 5
            continue
        elif i == 26:
            continue
        elif i == 27:
            continue
        elif i == 28:
            continue
        elif i == 30:
            continue
        x *= i
    x += 1
    return x

def main():
    N = int(input())
    print(solve(N))

if __name__ == '__main__':
    main()
