b = input()
A =  int(b.split()[0])
N =  int(b.split()[1])
while  N <= 0:
    N = int(input())
soma = 0
for num in range(A,(A+N)):
    soma = soma + num
print(soma)