X = 0
Y = 1

def solve(H: int, W: int, M: int, obstacles: list) -> int:
    cnt = 1
    board = [[0]*W for _ in range(H)]
    for o in obstacles:
        board[o[X]-1][o[Y]-1] = -1

    # 横 -> 縦
    for idx, now in enumerate(board[0]):
        if idx == 0:
            continue

        if now == -1:
            break

        i = 0
        while i < H and board[i][idx] != -1:
            board[i][idx] = 1
            cnt += 1
            i += 1

    # 横 -> 縦
    idx_1 = 1
    while idx_1 < H and board[idx_1][0] != -1:
        for idx_2, now in enumerate(board[idx_1]):
            if now == 1:
                continue
            if now == -1:
                break
            board[idx_1][idx_2] = 1
            cnt += 1
        idx_1 += 1
    return cnt

def main():
    H, W, M = map(int, input().split())
    obstacles = [list(map(int, input().split())) for _ in range(M)]

    print(solve(H, W, M, obstacles))

if __name__ == '__main__':
    main()
