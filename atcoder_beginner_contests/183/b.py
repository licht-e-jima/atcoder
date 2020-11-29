sx, sy, gx, gy = map(int, input().split())
print(sx - sy * (sx - gx) / (sy + gy))
