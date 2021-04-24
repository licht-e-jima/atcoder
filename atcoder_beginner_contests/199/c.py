N = int(input())
S = list(input())
Q = int(input())

from collections import deque
queries = deque()
fliped = False
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1 and not fliped:
        queries.append([a, b])
    elif t == 1 and fliped:
        if a <= N:
            a += N
        else:
            a -= N
        if b <= N:
            b += N
        else:
            b -= N
        queries.append([a, b])
    elif t == 2:
        fliped = not fliped

while len(queries) > 0:
    a, b = queries.popleft()
    s_a = S[a-1]
    s_b = S[b-1]
    S[a-1] = s_b
    S[b-1] = s_a

if not fliped:
    print(''.join(S))
else:
    print(''.join(S[N:]) + ''.join(S[:N]))
