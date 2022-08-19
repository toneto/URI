nome = input()
salario= float(input())
vendas = float(input())

total = salario + (vendas / 100) * 15

print("TOTAL = R$ %.2f" %total)