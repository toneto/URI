valor = int(input())

n100 = valor // 100
n50 = (valor % 100) // 50
n20 = ((valor % 100) % 50) // 20
n10 = (((valor % 100) % 50) % 20) // 10
n5 = ((((valor % 100) % 50) % 20) % 10) // 5
n2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
n1 = (((((valor % 100) % 50) % 20) % 10) % 5) % 2

print(valor)
print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")