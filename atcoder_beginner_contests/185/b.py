from itertools import chain

def solve(N: int, M: int, T: int, cafe: list) -> bool:
    if len(cafe) == 0:
        return N > T

    arr = list(chain.from_iterable(cafe))
    arr.append(0)
    arr.append(T)
    arr.sort()
    in_cafe = False
    battery = N
    before = 0
    for t in arr[1:]:
        doing = t - before
        if in_cafe:
            battery = min(N, battery + doing)
        else:
            battery -= doing
            if battery <= 0:
                return False

        in_cafe = not in_cafe
        before = t

    return True

def main():
    N, M, T = map(int, input().split())
    cafe = [map(int, input().split()) for _ in range(M)]
    can = solve(N, M, T, cafe)
    print("Yes" if can else "No")

if __name__ == "__main__":
    main()
