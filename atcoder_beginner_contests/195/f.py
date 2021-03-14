from itertools import combinations
from math import gcd
from functools import lru_cache
import subprocess



@lru_cache(maxsize=None)
def present(tup: tuple) -> bool:
    if len(tup) < 2:
        return True
    elif len(tup) == 2:
        # res_1 = subprocess.check_output(f"factor {tup[0]}")
        # factor_1 = set(res_1[len(tup[0]):].split())
        # res_2 = subprocess.check_output(f"factor {tup[1]}")
        # factor_2 = set(res_2[len(tup[1]):].split())
        # return len(factor_1 & factor_2) == 0
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
