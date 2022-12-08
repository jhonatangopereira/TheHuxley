patrimonioTotal = float(input())
declarou = int(input())
patrimonioInvestido = float(input())
multa = input()

if patrimonioTotal >= 1000000:
    if patrimonioInvestido > (0.20*patrimonioTotal):
        if declarou < (patrimonioInvestido - 0.10*patrimonioInvestido):
            if multa == 'sim':
                categoria = 'Crime'
            elif multa == 'nao':
                categoria = 'Imposto+Multa'
            valorMulta = 0.15*patrimonioInvestido
        else:
            if multa == 'sim':
                categoria = 'Crime'
            else:
                categoria = 'Imposto'
            valorMulta = 0.0
        imposto = 0.15*patrimonioInvestido
    elif patrimonioInvestido <= (0.20*patrimonioTotal):
        categoria = "Isento"
        imposto = 0.0
        valorMulta = 0.0
    print(f'{categoria}\n{imposto:.1f}\n{valorMulta:.1f}')
elif patrimonioTotal < 1000000:
    if patrimonioInvestido > (0.20*patrimonioTotal):
        categoria = "Imposto"
        imposto = 0.15*patrimonioTotal
        valorMulta = 0.0
        print(f'{categoria}\n{imposto:.1f}\n{valorMulta:.1f}')
    else:
        categoria = "Isento"
        imposto = 0.0
        valorMulta = 0.0
        print(f'{categoria}\n{imposto:.1f}\n{valorMulta:.1f}')
