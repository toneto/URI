N = input().split(' ')
A = float(N[0])
B = float(N[1])
C = float(N[2])
D = float(N[3])

if(B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0 ):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")