valores = input().split(' ')
A = int(valores[0])
B = int(valores[1])
if ((B % A) == 0) or (A % B == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")