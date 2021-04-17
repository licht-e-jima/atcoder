from itertools import combinations
from math import gcd
from functools import lru_cache
import subprocess



@lru_cache(maxsize=None)
def present(tup: tuple) -> bool:
    if len(tup) < 2:
        return True
    elif len(tup) == 2:
        return gcd(*tup) == 1

    for pair in combinations(tup, 2):
        if not present(pair):
            return False

    return True

A, B = map(int, input().split())

candidates = [i for i in range(A, B+1)]

cnt = 0
for i in range(0, B-A+2):
    for combi in combinations(candidates, i):
        if present(combi):
            cnt += 1

print(cnt)
