valores = input().split(' ')
x = float(valores[0])
y = float(valores[1])


if x > 0 and y > 0:
    print("Q1")
elif x < 0 < y:
    print("Q2")
elif x < 0 and y <0:
    print("Q3")
elif x > 0 > y:
    print("Q4")
elif x == 0 and y == 0:
    print("Origem")
elif y != 0 and x == 0:
    print("Eixo Y")
elif x != 0 and y == 0:
    print("Eixo X")
