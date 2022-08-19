N = int(input())
if 2 < N < 1000:
  for i in range(1,11):
    tab = N * i
    print("%d x %d = %d" % (i, N, tab))