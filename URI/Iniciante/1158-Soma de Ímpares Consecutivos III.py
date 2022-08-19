n = int(input())
count = 0
while(count < n):
  lista = []
  x, y = map(int, input().split())
  while(len(lista) != y):
    if(x % 2 == 0):
      x += 1
    else:
      lista.append(x)
      x += 2
  print(sum(lista))
  count += 1