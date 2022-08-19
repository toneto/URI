peca1 = input().split(' ')
peca2 = input().split(' ')

codigo1 = float(peca1[0])
numeros1 = float(peca1[1])
preco1 = float(peca1[2])

codigo2 = float(peca2[0])
numeros2 = float(peca2[1])
preco2 = float(peca2[2])

soma1 = numeros1 * preco1
soma2 = numeros2 * preco2
soma = soma1 + soma2

print("VALOR A PAGAR: R$ %.2f" %soma)