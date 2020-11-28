def go_down(down: int, x: int, y: int) -> int:
    if 2 * x <= y:
        return 2 * x * (down - 1) + x
    else:
        return y * (down - 1) + x

def go_up(up: int, x: int, y: int) -> int:
    if 2 * x <= y:
        return 2 * x * up + x
    else:
        return y * up + x

def pass_corridor(x) -> int:
    return x

def solve(a, b, x, y) -> int:
    if a > b:
        return go_down(a - b, x, y)
    elif a < b:
        return go_up(b - a, x, y)
    else:
        return pass_corridor(x)

def main():
    a, b, x, y = map(int, input().split())
    print(solve(a, b, x, y))

if __name__ == '__main__':
    main()
