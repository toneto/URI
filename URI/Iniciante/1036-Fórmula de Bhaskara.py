import math

N = input().split(' ')
A = float(N[0])
B = float(N[1])
C = float(N[2])

delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")

else:
    rais1 = (-B + math.sqrt(delta)) / (2 * A)
    rais2 = (-B - math.sqrt(delta)) / (2 * A)
    print("R1 = %.5f" %rais1)
    print("R2 = %.5f" %rais2)