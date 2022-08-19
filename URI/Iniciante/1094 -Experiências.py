N = int(input())
cobaias, rato, sapo, coelho = 0, 0, 0, 0

for i in range(N):
    Quantia,Tipo=input().split()
    str(Tipo)
    cobaias += int(Quantia)
    if Tipo== 'C':
        coelho += int(Quantia)
    elif Tipo =='R':
        rato += int(Quantia)
    elif Tipo == 'S':
        sapo += int(Quantia)

print('Total: %d cobaias' % cobaias)
print('Total de coelhos: %d' %coelho)
print('Total de ratos: %d' %rato)
print('Total de sapos: %d' %sapo)
print('Percentual de coelhos: %.2f' % float(((100*coelho) / cobaias)), '%')
print('Percentual de ratos: %.2f' % float(((100*rato) / cobaias)), '%')
print('Percentual de sapos: %.2f' % float(((100*sapo) / cobaias)), '%')