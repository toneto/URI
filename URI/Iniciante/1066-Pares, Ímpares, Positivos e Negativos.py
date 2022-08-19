n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
lista = [n1,n2,n3,n4,n5]

i = 0
pares = []
while i < len(lista):
	if lista[i] % 2 == 0:
		pares.append(lista[i])
	i = i + 1

inpar = len(lista) - len(pares)

i = 0
positivos = []
while i < len(lista):
	if lista[i] > 0:
		positivos.append(lista[i])
	i = i + 1

i = 0
negativos = []
while i < len(lista):
	if lista[i] < 0:
		negativos.append(lista[i])
	i = i + 1

print("%i valor(es) par(es)" %len(pares))
print("%i valor(es) impar(es)" %inpar)
print("%i valor(es) positivo(s)" %len(positivos))
print("%i valor(es) negativo(s)" %len(negativos))