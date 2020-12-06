from typing import List

def solve(H: int, W: int, S: List[int]) -> int:
    pass

def main():
    H, W = map(int, input().split())
    S = [input().split() for _ in range(H)]
    print(solve(H, W, S))

if __name__ == '__main__':
    main()
