from functools import lru_cache

MAX_DEPTH = 499

@lru_cache(maxsize=None)
def rec_combi(n: int, r: int) -> int:
    if r == 1:
        return n

    return rec_combi(n - 1, r - 1) * n // r

def calc_combi(n: int, r: int) -> int:
    numerators = [n-i for i in range(r)]
    denominators = list(range(2, r+1))

    def factorization(num: int):
        temp = num
        for i in range(2, int(-(-num**0.5//1))+1):
            if temp%i==0:
                while temp%i==0:
                    temp //= i
                    yield i

        if temp!=1:
            yield temp

    def devide(denominator):
        for i in range(len(numerators)):
            if numerators[i] % denominator == 0:
                numerators[i] = int(numerators[i]/denominator)
                break
        else:
            for f in factorization(denominator):
                devide(f)

    for d in reversed(denominators):
        devide(d)

    factorization = 1
    for n in numerators:
        factorization *= n
    return  factorization


def combinations(n: int, r: int) -> int:
    if n - r < r:
        return combinations(n, n - r)
    elif r <= MAX_DEPTH:
        return rec_combi(n, r)
    else:
        return calc_combi(n, r)
