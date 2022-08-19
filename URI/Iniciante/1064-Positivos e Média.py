n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
lista = [n1,n2,n3,n4,n5,n6]

positivos = []
i = 0

while i < len(lista):
	if lista[i] > 0:
		positivos.append(lista[i])
	i = i + 1

i = 0

soma = 0
while i < len(positivos):
	soma = soma + positivos[i]
	i = i + 1

media = soma / len(positivos)

print("%i valores positivos" %len(positivos))
print("%.1f" %media)