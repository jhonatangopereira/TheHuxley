total = float(input())
pessoas = int(input())
if total > 0 and pessoas > 0:
  soma = 0
  valor_maior = 0

  for i in range(pessoas):
    nome = input()
    valor_atual = float(input())
    soma += valor_atual
    if valor_atual > valor_maior: 
      x = f'{nome} pagou R$ {valor_atual:.1f}'
      valor_maior = valor_atual
    
  if soma == total:
    print(x)
    print(0)
  elif soma > total:
    print(x)
    diferenca = soma - total 
    print(f'Valor excedente: sobra R$  {diferenca:.1f}')
  elif total > soma:
    print(x)
    diferenca = total - soma
    print(f'Valor insuficiente: falta R$  {diferenca:.1f}')
else:
  print('Nao ha conta ou funcionario suficiente para pagar a conta')
