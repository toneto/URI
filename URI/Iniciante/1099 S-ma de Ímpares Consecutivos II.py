y = int(input())
for i in range(y):
  count = 0
  x = input().split()
  a = int(x[0])
  b = int(x[1])
  if(a >= b):
    if(b % 2 == 0):
      for j in range(b, a):
        if(j % 2 != 0):
          count += j
    else:
      for j in range(b + 1, a):
        if(j % 2 != 0):
          count += j
  else:
    if(a % 2 == 0):
      for j in range(a, b):
        if(j % 2 != 0):
          count += j
    else:
      for j in range(a + 1, b):
        if(j % 2 != 0):
          count += j
  print(count)