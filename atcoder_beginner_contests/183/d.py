N, W = map(int, input().split())

# S, T, P
times = [0]*(2*10**5+1)
for i in range(N):
  S, T, P = map(int, input().split())
  times[S] += P
  times[T] -= P

amount = 0
for t in times:
  amount += t
  if amount > W:
    print('No')
    break
else:
  print('Yes')
