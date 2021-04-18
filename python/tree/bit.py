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
