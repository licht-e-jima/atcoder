def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.extend([i for _ in range(cnt)])

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr

def devide(numerators, denominator):
    for i in range(11):
        if numerators[i] % denominator == 0:
            numerators[i] = int(numerators[i]/denominator)
            break
    else:
        for f in factorization(denominator):
            devide(numerators, f)

def solve(L: int) -> int:
    numerators = [L-i-1 for i in range(11)]
    denominators = list(range(2, 12))
    for d in reversed(denominators):
        devide(numerators, d)

    pi = 1
    for n in numerators:
        pi *= n

    return pi

def main():
    L = int(input())
    print(solve(L))

if __name__ == '__main__':
    main()
