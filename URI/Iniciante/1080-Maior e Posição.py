count = 0
for i in range(100):
  x = int(input())
  if(count < x):
    count = x
    posicao = i + 1
print(count)
print(posicao)