i = 0
count = 0
while(i < 2):
  x = float(input())
  if(x < 0) or (x > 10):
    print('nota invalida')
  else:
    count += x
    i += 1
cal = count / 2
print('media = %.2f' %cal)