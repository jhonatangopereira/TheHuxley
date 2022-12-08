menor = 100000
menor_jogador = ''
maior = 0
maior_jogador = ''
soma_de_pontos = 0
qtd_jogadores = 0

while True:
  nome_jogador = input()
  if nome_jogador == "sair":
    break
  quantidade_pontos = int(input())
  soma_de_pontos += quantidade_pontos
  qtd_jogadores += 1

  if quantidade_pontos > maior:
    maior_jogador = nome_jogador
    maior = quantidade_pontos
  if quantidade_pontos < menor:
    menor_jogador = nome_jogador
    menor = quantidade_pontos

if maior == 0:
  print("Nenhum jogador foi registrado.")
else:
  print(menor_jogador)
  print(maior_jogador)
  media = soma_de_pontos / qtd_jogadores
  print(f"{media:.2f}")