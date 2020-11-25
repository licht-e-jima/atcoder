from typing import List, Iterable


class CombiIter:
    def __init__(self, a: List[int]) -> None:
        self.a = a
        self.len = len(a)
        self.min = a[0]
        self.result_cache = {i for i in a}
        self.combi_cache = {}

    def is_cached(self, n: int) -> bool:
        return n in self.result_cache

    def combinations(self, n: int) -> Iterable:
        """
        ref: https://docs.python.org/3/library/itertools.html#itertools.combinations
        """
        indices = list(range(n))
        border = self.len - n
        tuple_indices = tuple(indices)
        if tuple_indices not in self.combi_cache:
            yield tuple_indices, tuple(self.a[i] for i in indices)

        while True:
            for i in reversed(range(n)):
                if indices[i] != i + border:
                    break
            else:
                return

            indices[i] += 1
            for j in range(i+1, n):
                indices[j] = indices[j-1] + 1

            tuple_indices = tuple(indices)
            if tuple_indices not in self.combi_cache:
                yield tuple_indices, tuple(self.a[i] for i in indices)

    def is_feasible(self, n: int) -> bool:
        min_val = self.min
        if n in self.result_cache:
            return True

        for m in range(1, self.len):
            if min_val > n:
                break

            for indices, combi in self.combinations(m):
                val = sum(combi)
                self.combi_cache[indices] = val
                self.result_cache.add(val)
                if val == n:
                    return True

            min_val = self.combi_cache[tuple(range(m))]

        return False

def solve(N: int, T: int, A: List[int]) -> int:
    """
    最初に A を小さい順に並べて全ての総和を計算する
    総和が T 以下なら総和を答えとして返す
    総和が T より大きければ
    m を最大として T から 1 ずつ減らして、 sum = m となる組み合わせがあればそれを返す
    組み合わせの探し方は総和から引き算して T 以下になるようにする
    組み合わせはキャッシュする
    なければ 0 を返す
    """
    A.sort()
    a = list(filter(lambda i: i <= T, A))
    total = sum(A)
    diff = total - T
    if diff <= 0:
        return total
    elif len(a) == 0:
        return 0

    if any(i == diff for i in a):
        return T

    combi_iter = CombiIter(a)

    second_min = total - a[0]
    if second_min <= T:
        return second_min

    for n in range(0, T - a[0] + 1):
        if T - n == 273555143:
            x = 1 + 1

        if combi_iter.is_feasible(n + diff):
            return T - n
    else:
        raise Exception()


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, T, A))

if __name__ == '__main__':
    main()
    N, T = 7, 273599681
    A = list(map(int, '6706927 91566569 89131517 71069699 75200339 98298649 92857057'.split()))
    print(solve(N, T, A))

