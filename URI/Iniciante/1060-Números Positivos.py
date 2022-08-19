n1 = []
n1.append(float(input()))
n1.append(float(input()))
n1.append(float(input()))
n1.append(float(input()))
n1.append(float(input()))
n1.append(float(input()))

saida = 0
for n in n1:
    if (float(n)>0):
        saida= saida + 1

print(saida, "valores positivos")