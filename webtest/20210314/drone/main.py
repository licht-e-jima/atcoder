import sys

from solve import solve

def main(lines):
    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))

    H, W = map(int, lines[0].split())
    S = [list(l) for l in lines[1:-1]]
    T = lines[-1]
    ans = solve(H, W, S, T)
    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
