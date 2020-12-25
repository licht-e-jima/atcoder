H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

minimums = [min(row) for row in A]
minimum = min(minimums)

ans = 0
for row in A:
    for block in row:
        ans += block - minimum

print(ans)
