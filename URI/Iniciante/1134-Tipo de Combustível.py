produto = int(input())
alcool = 0
gasolina = 0
diesel = 0

while produto != 4:
    if produto == 1:
        alcool += 1
    elif produto == 2:
        gasolina += 1
    elif produto == 3:
        diesel += 1
    produto = int(input())

print("MUITO OBRIGADO")
print("Alcool: %d" % alcool)
print("Gasolina: %d" % gasolina)
print("Diesel: %d" % diesel)