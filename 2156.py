volume_inicial = int(input())
entradas_de_volume = int(input())

for i in range(entradas_de_volume):
  apertos = int(input())
  if volume_inicial + apertos >= 100:
    volume_inicial = 100
  elif volume_inicial + apertos <= 0:
    volume_inicial = 0
  else:
    volume_inicial += apertos
print(volume_inicial)