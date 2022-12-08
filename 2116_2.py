carne = input()

if carne == 'C' or carne == 'BF' or carne == 'BS':
  paoDeAlho = input()
  bebidaAdulto = input()
  bebidaKid = input()
  quantKids = int(input())
  quantAdulto = int(input())
  VALOR_CERVEJA = 8
  VALOR_REFRIGERANTE = 6
  
  if carne == 'C':
    valorChurrasco = (6.4 + 1.8 + 1.5) * quantAdulto
  elif carne == 'BF':
    valorChurrasco = (8 + 2.7) * quantAdulto
  elif carne == 'BS':
    valorChurrasco = (8 + 2.25) * quantAdulto
  valorChurrasco += 6.4 * quantKids

  if bebidaAdulto == 'S':
    valorChurrasco += (2 * 8) * quantAdulto
  if bebidaKid == 'S':
    valorChurrasco += (0.5 * 6) * quantKids
  if paoDeAlho == 'S':
    valorChurrasco *= 0.98
  print(f'R$: {valorChurrasco:.2f}')
else:
  print('Opção inv�lida.')
