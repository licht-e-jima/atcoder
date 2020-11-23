def solve(r, c):
    if r == 0 and c == 0:
        return 0
    elif r == c:
        return 1
    elif r <= 3 and c <= 3 and r + c <= 3:
        return 1
    elif r % 2 == c % 2:
        return 2
    elif c - r  <= 3:
        return 2
    elif r == 0 and c == 5:
        return 2
    else:
        return 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    rgoal = r2 - r1 if r2 >= r1 else r1 - r2
    cgoal = c2 - c1 if c2 >= c1 else c1 - c2
    vector = (rgoal, cgoal) if rgoal <= cgoal else (cgoal, rgoal)
    print(solve(*vector))

if __name__ == "__main__":
    main()
