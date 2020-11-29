from itertools import permutations

def main(n, k, t):
	num_of_patterns = 1
	for i in range(1, n):
		num_of_patterns *= i

	t12 = t[0][1]
	if all(map(lambda i: all(map(lambda j: j in (0, t12), i)), t)):
		if n * t12 == k:
			print(num_of_patterns)
		else:
			print(0)
		return

	def mapping(per):
		def fun(i):
			if i == 0:
				return t[0][per[0]]
			elif i == len(per):
				return t[per[i - 1]][0]
			else:
				return t[per[i - 1]][per[i]]
		return fun

	patterns = list(filter(
		lambda s: s == k,
		[
			sum(map(mapping(per), range(n)))
			for per
			in permutations(range(1, n), n - 1)
		]
	))
	print(len(patterns))



n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
main(n, k, t)
