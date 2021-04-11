from copy import deepcopy
from typing import *
import math
import functools
from collections import deque
import itertools

str_map: Dict[str,int] = {}

def get_num(s: str) -> int:
    n = ""
    for c in s:
        n += str(str_map[c])
    return int(n)

def solve(s1: str, s2: str, s3: str) -> List[Union[int,str]]:
	used = set(s1) | set(s2) | set(s3)
	for c in used:
		str_map[c] = 0
	starts = list({s1[0], s2[0], s3[0]})
	keys = list(str_map.keys())
	for i, c in enumerate(starts):
		starts[i] = keys.index(c)

	if len(str_map) > 10:
		return ["UNSOLVABLE"]

	for tup in itertools.permutations(range(10), len(str_map)):
		if any(map(lambda i: tup[i] == 0, starts)):
			continue

		for i, k in enumerate(str_map):
			str_map[k] = tup[i]

		n1 = get_num(s1)
		n2 = get_num(s2)
		n3 = get_num(s3)
		if n3 == n1 + n2:
			return [n1, n2, n3]
	else:
		return ["UNSOLVABLE"]

def main():
	S1 = input()
	S2 = input()
	S3 = input()
	ans = solve(S1, S2, S3)
	for a in ans:
		print(a)


if __name__ == "__main__":
	main()
