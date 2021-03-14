from functools import lru_cache

N_str = input()

@lru_cache(maxsize=None)
def get_comma(n_str: str) -> int:
    N_len = len(n_str)
    if N_len <= 3:
        return 0

    N = int(n_str)
    max_comma = (N_len-1) // 3

    max_min = 10**(max_comma*3)
    print(max_min, max_comma, N)
    return (N-max_min+1)*max_comma + get_comma(str(max_min-1))

print(get_comma(N_str))
