x,y = map(int, input().split())
lista = []
for i in range(1,y+1):
    lista.append(i)
    if (len(lista) == x):
        print(' '.join(map(str, lista)))
        lista = []