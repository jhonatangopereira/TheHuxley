N = int(input())

for i in range(N):
  V1, V2, D1, D2 = map(int, input().split())
  rodadas_para_bezaliel_ganhar = int(round(V1 / D2 + 0.49, 0))
  clodes_vence = False
  
  for j in range(rodadas_para_bezaliel_ganhar):
    possibilidade_de_dano = (rodadas_para_bezaliel_ganhar - j) * D1
    if possibilidade_de_dano >= V2:
      clodes_vence = True
      break
    D1 += 50
  print(f"{'Clodes' if clodes_vence else 'Bezaliel'}")
