n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
lista = [n1,n2,n3,n4,n5]

pares = []
i = 0

while i < len(lista):
	if lista[i] % 2 == 0:
		pares.append(lista[i])
	i = i + 1

print("%i valores pares" %len(pares))