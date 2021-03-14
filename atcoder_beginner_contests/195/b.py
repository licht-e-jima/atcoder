from math import floor, ceil

A, B, W = map(int, input().split())

W_gram = W * 1000

if A == B:
    able = W_gram % A == 0
else:
    able = (W_gram//A - W_gram//B) > 0

significancy = 1000

if able:
    minimum = ceil(W_gram/B)
    maximum = floor(W_gram/A)
    print(minimum, maximum)
else:
    print("UNSATISFIABLE")
