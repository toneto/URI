while True:
    lista = input()
    x, y = lista.split()
    X = int(x)
    Y = int(y)
    if X == Y:
        break
    else:
        if X > Y:
            print("Decrescente")
        else:
            print("Crescente")