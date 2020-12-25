N = int(input())

# print(N - N//8 - N//10 + N//80)

def oct(n):
    dig = 0
    while n > 8 ** dig:
        if (n // (8 ** dig)) % 8 == 7:
            return False

        dig += 1

    return True

def dect(n):
    dig = 0
    while n > 10 ** dig:
        if (n // (10 ** dig)) % 10 == 7:
            return False
        dig += 1
    return True

cnt = 0
for i in range(1, N+1):
    if oct(i) and dect(i):
        cnt += 1

print(cnt)
