from functools import lru_cache

def solve_1(n: int) -> float:
    return 100 - n

def solve_2(n1: int, n2: int) -> float:
    @lru_cache(maxsize=None)
    def expect(a: int, b: int) -> float:
        '''a <= b'''
        if b == 100:
            return 0
        elif a == b:
            return expect(a, b+1) + 1
        else:
            return (a/(a+b)) * (expect(a+1, b) + 1) \
                + (b/(a+b)) * (expect(a, b+1) + 1)

    return expect(n1, n2)

def solve_3(n1: int, n2: int, n3: int) -> float:
    @lru_cache(maxsize=None)
    def expect(a: int, b: int, c: int) -> float:
        '''a <= b <= c'''
        if c == 100:
            return 0
        elif a == b == c:
            return expect(a, b, c+1) + 1
        elif a == b:
            return 2 * (b/(a+b+c)) * (expect(a, b+1, c) + 1) \
                + (c/(a+b+c)) * (expect(a, b, c+1) + 1)
        elif b == c:
            return (a/(a+b+c)) * (expect(a+1, b, c) + 1) \
                + 2 * (c/(a+b+c)) * (expect(a, b, c+1) + 1)
        else:
            return (a/(a+b+c)) * (expect(a+1, b, c) + 1) \
                + (b/(a+b+c)) * (expect(a, b+1, c) + 1) \
                + (c/(a+b+c)) * (expect(a, b, c+1) + 1)

    return expect(n1, n2, n3)

def main():
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[1] == 0:
        print(solve_1(l[2]))
    elif l[0] == 0:
        print(solve_2(l[1], l[2]))
    else:
        print(solve_3(*l))

if __name__ == '__main__':
    main()
