carne = input()

if carne == 'C' or carne == 'BF' or carne == 'BS':
  paoDeAlho = input()
  bebidaAdulto = input()
  bebidaKid = input()
  quantKid = int(input())
  quantAdulto = int(input())
  if carne == 'C':
    calculo = (6.4 + 1.8 + 1.5)*quantAdulto + x + y
  elif carne == 'BF':
    calculo = (8 + 2.7)*quantAdulto
  elif carne == 'BS':
    calculo = (8 + 2.25)*quantAdulto
  if bebidaAdulto == 'S':
    calculo += 2*8*quantAdulto
  if bebidaKid == 'S':
    y = 0.5*6*quantKid
  calculo += 6.4 * quantKid
  if paoDeAlho == 'N':
    calculo = calculo - calculo * 0.02
  print(f'R$: {calculo:.2f}')
else:
  print('Opção inválida.')
