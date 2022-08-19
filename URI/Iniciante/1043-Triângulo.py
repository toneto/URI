valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

triangulo = sorted(valores)
a1 = float(triangulo[0])
b1 = float(triangulo[1])
c1 = float(triangulo[2])

if c1 < (b1 + a1):
    peri = a + b + c
    print("Perimetro = %.1f" %peri)
else:
    area = ((a + b) * c ) / 2
    print("Area = %.1f" %area)