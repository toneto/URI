novo = 1
v_inter = 0
v_gremio = 0
empate = 0
grenais = 0

while novo == 1:
  gols = input().split(" ")
  inter = int(gols[0])
  gremio = int(gols[1])

  if inter > gremio:
    v_inter+= 1
  elif gremio > inter:
    v_gremio+= 1
  elif inter == gremio:
    empate+= 1

  grenais+= 1
  print("Novo grenal (1-sim 2-nao)")
  novo = int(input())

print("%d grenais" %grenais)
print("Inter:%d" %v_inter)
print("Gremio:%d" %v_gremio)
print("Empates:%d" %empate)

if v_inter > v_gremio:
  print("Inter venceu mais")
elif v_gremio > v_inter:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")