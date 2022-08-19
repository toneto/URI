N = int(input())
for i in range(N):
  v = input().split()
  a = float(v[0])
  b = float(v[1])
  c = float(v[2])
  media = ((a * 2) + (b * 3) + (c * 5)) / 10
  print('%.1f' % media)