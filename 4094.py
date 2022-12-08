pontuacao = [int(input()), int(input()), int(input())]

if (pontuacao[0] < pontuacao[1] or pontuacao[1] < pontuacao[2]) or (pontuacao[0] > 100 or pontuacao[1] > 100 or pontuacao[2] > 100):
  print("Violacao das restricoes")
else:
  trofeus = 1
  placas = 0
  if pontuacao[0] == pontuacao[1]:
    trofeus += 1
    if pontuacao[1] == pontuacao[2]:
      trofeus += 1
    else:
      placas += 1
  else:
    placas += 1
    if pontuacao[1] == pontuacao[2]:
      placas += 1
  print(f"{trofeus} trofeu{'s' if trofeus > 1 else ''} e {placas} placa{'s' if placas > 1 else ''}")
