idade = int(input())
tipo = input()
if tipo == 'azar' or tipo =='mmorpg' or tipo == 'moba' or tipo == 'casual':
  if tipo == 'azar':
    if idade >= 21 and idade <= 130:
      print('Pode entrar!')
    elif idade <21 and idade >=0:
      print('Volte daqui há alguns anos.')
    else:
      print('Idade invalida.')
  elif tipo == 'mmorpg':
    if idade >=14 and idade >=130:
      print('Pode entrar!')
    elif idade < 14 and idade >=0:
      print('Volte daqui há alguns anos.')
    else:
      print('Idade invalida.')
  elif tipo == 'moba':
    if idade >= 10 and idade <=130:
      print('Pode entrar!')
    elif idade <10 and idade >=0:
      print('Volte daqui há alguns anos.')
    else:
      print('Idade invalida.')
  elif tipo == 'casual':
    if idade >= 0 and idade <=130:
      print('Pode entrar!')
    else:
      print('Idade invalida.')
    
else:
  print('Jogo invalido.')
