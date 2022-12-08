patrimonio = float(input())
patrimonio_declarado_exterior = int(input())
patrimonio_investido_exterior = float(input())
ja_pagou_multa = input()

imposto = 0
multa = 0
if patrimonio_investido_exterior > patrimonio * 0.20:
  imposto = patrimonio_investido_exterior * 0.15
  saida = "Imposto"
  if patrimonio_declarado_exterior < 0.9 * patrimonio_investido_exterior:
    multa = imposto
    saida = "Imposto+Multa"
  if ja_pagou_multa == "sim":
    saida = "Crime"
else:
  saida = "Isento"
print(f"{saida}\n{imposto:.1f}\n{multa:.1f}")