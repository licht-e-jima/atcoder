from math import sin, cos, sqrt
from typing import Tuple

PI = 3.141592653589793238462643383279

def solve(N: int, x0: int, y0: int, xN_2: int, yN_2: int) -> Tuple[float, float]:
    angle = 2 * PI / N
    center = ((x0+xN_2)/2, (y0+yN_2)/2)

    zero = [x0 - center[0], y0 - center[1]]
    one = [
        cos(angle) * zero[0] - sin(angle) * zero[1],
        sin(angle) * zero[0] + cos(angle) * zero[1],
    ]
    return center[0] + one[0], center[1] + one[1]

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN_2, yN_2 = map(int, input().split())
    x1, y1 = solve(N, x0, y0, xN_2, yN_2)
    print(f"{x1} {y1}")

if __name__ == '__main__':
    main()
