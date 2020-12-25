class BIT:
    """binary indexed tree

    Attributes:
        N (int): 要素数
        data (list): インデックスのデータ(途中までの合計)
        elem (list): 各要素の値(なくても成立する)
    """
    N: int
    data: list
    elem: list

    def __init__(self, N: int):
        """要素数 n のBITを構築する

        Args:
            n (int): 要素数
        """
        self.N = N
        self.data = [0]*(N+1)
        self.elem = [0]*(N+1)

    def sum(self, i: int) -> int:
        """i 番目までの値の合計を返す

        Args:
            i (int): インデックス

        Returns:
            int: 合計
        """
        s = 0
        while i > 0:
            s += self.data[i]
            # LSB を引いて次の要素にいく
            i -= i & -i
        return s

    def add(self, i, x):
        """i 番目の要素に x を加算する
        それに従って上位のノードにも加算していく

        Args:
            i (int): インデックス
            x (int): 加算値
        """
        # assert i > 0
        self.elem[i] += x
        while i <= self.N:
            self.data[i] += x
            # LSB を足して次の要素にいく
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.elem[i]
        return self.sum(j) - self.sum(i)

    def query_1(self, i: int, y: int):
        val = self.get(i)
        new_val = val ^ y
        self.add(i, new_val-val)

    def query_2(self, i: int, j: int) -> int:
        pass

def query_2(bit: BIT, x: int, y: int) -> int:
    ans = A[x-1]
    for a in A[x:y]:
        ans = ans ^ a
    return ans

T= 0
X = 1
Y = 2
QUERY_1 = 1
QUERY_2 = 2

def solve(N: int, Q: int, A: list, queries: list) -> list:
    bit = BIT(N)
    for i, a in enumerate(A):
        bit.add(i, a)

    answers = []
    for q in queries:
        if q[T] == QUERY_1:
            query_1(bit, q[X], q[Y])
        elif q[T] == QUERY_2:
            ans = query_2(bit, q[X], q[Y])
            answers.append(ans)

    return answers

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    ans = solve(N, Q, A, queries)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
