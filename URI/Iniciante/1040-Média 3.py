notas = input().split(' ')
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10)
print("Media: %.1f" %media)
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" %exame)
    MF = (media + exame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" %MF)