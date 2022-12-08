N = int(input())
numero_maior_frequencia = 0
maior_frequencia = 0

for i in range(2, 8):
  frequencia_atual = 0
  resultado = N
  while True:
    if resultado % i == 0:
      frequencia_atual += 1
      resultado /= i
    else:
      if frequencia_atual > maior_frequencia:
        numero_maior_frequencia = i
        maior_frequencia = frequencia_atual
      break
print(f"mostFrequent: {numero_maior_frequencia}, frequency: {maior_frequencia}")