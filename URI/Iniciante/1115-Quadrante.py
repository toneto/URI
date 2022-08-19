x,y = 1,1
while x != 0 or y != 0:
    valores = input().split(' ')
    x = float(valores[0])
    y = float(valores[1])
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 < y:
        print("segundo")
    elif x < 0 and y <0:
        print("terceiro")
    elif x > 0 > y:
        print("quarto")