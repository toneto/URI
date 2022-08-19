Di = input().split(" ")
di = int(Di[1])

Hi = input().split(" ")
hi = int(Hi[0])
mi = int(Hi[2])
si = int(Hi[4])

Df = input().split(" ")
df = int(Df[1])

Hf = input().split(" ")
hf = int(Hf[0])
mf = int(Hf[2])
sf = int(Hf[4])

dia = df - di
hora = hf - hi
minuto = mf - mi
segundos = sf - si

if hora < 0:
    hora = 24 + hora
    dia = dia - 1

if minuto < 0:
    minuto = 60 + minuto
    hora = hora - 1

if segundos < 0:
    segundos = 60 + segundos
    minuto = minuto - 1

if dia <= 0:
    dia = 0

print("%i dia(s)" % dia)
print("%i hora(s)" % hora)
print("%i minuto(s)" % minuto)
print("%i segundo(s)" % segundos)