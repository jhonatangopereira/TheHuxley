total_de_pregos = 0
while True:
  pregos_por_quadro = int(input())
  if pregos_por_quadro % 2 != 0: break

  total_de_pregos += pregos_por_quadro
caixas_de_pregos = total_de_pregos // 12
restante_de_pregos = total_de_pregos % 12

if restante_de_pregos > 0:
  caixas_de_pregos += 1
  restante_de_pregos = 12 - restante_de_pregos

print(f"{(caixas_de_pregos * 7.89):.2f}")
print(f"{restante_de_pregos}")