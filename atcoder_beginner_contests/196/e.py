from functools import partial
from typing import List, Tuple, Optional, Any, Dict

INF: int = 1 << 60

class Function:
    a: int
    b: int
    c: int

    def __init__(self):
        self.a = INF
        self.b = -INF
        self.c = 0

    def __call__(self, x: int) -> int:
        return min(self.a, max(self.b, x+self.c))

class Functions:
    def __init__(self, N: int, F: List[Tuple[int,int]]):
        self.N = N
        self.F = F
        self.G = self.__G(N, F)

    def __G(self, N: int, F: List[Tuple[int,int]]):
        g: Function = Function()

        for f in F:
            if f[1] == 1:
                g.a += f[0]
                g.b += f[0]
                g.c += f[0]
            elif f[1] == 2:
                g.a = max(g.a, f[0])
                g.b = max(g.b, f[0])
            else:
                g.a = min(g.a, f[0])

        return g

    def __call__(self, x: int) -> int:
        return self.G(x)

class FunctionsSingleton:
    f = None

    @classmethod
    def get(cls, N, F):
        if cls.f is not None:
            return cls.f

        cls.f = Functions(N, F)
        return cls.f

def solve(
    N: int,
    F: List[Tuple[int,int]],
    x: int,
) -> int:
    f = FunctionsSingleton.get(N, F)
    return f(x)


def main():
    N = int(input())
    F = [
        tuple(map(int, input().split()))
        for _ in range(N)
    ]
    Q = int(input())
    X = list(map(int, input().split()))
    for x in X:
        ans = solve(N, F, x)
        print(ans)

if __name__ == '__main__':
    main()
