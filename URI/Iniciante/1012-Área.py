valores = input().split(' ')

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

triangolo = (a*c)/2
circulo = 3.14159 * c**2
trapesio = ((a+b)*c)/2
quadrado = b*b
retangulo = a*b

print("TRIANGULO: %.3f" %triangolo)
print("CIRCULO: %.3f" %circulo)
print("TRAPEZIO: %.3f" %trapesio)
print("QUADRADO: %.3f" %quadrado)
print("RETANGULO: %.3f" %retangulo)