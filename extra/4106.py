n = int(input())
if n ==0:
    print('Sem termos para somar')
else:
    soma = ''
    x = 0
    y = 0
    cont = 6
    z = 4
    adiciona = 5

    for i in range(1, n+1):
        if i%2!=0:
            y += 1
            soma += f'{y} + '
            x+=y
        elif i == 2:
            x += 1/3
            soma += f'1/3 + '
        elif i == 4:
            x += 4/6
            soma += f'4/6 + ' 
        else:
            cont+= 3
            z+=adiciona
            x += z/(cont)
            soma += f'{z}/{cont} + '
            adiciona +=2
    

    
    print(f'S= {soma[0:-3]}')
    print(f'{x:.2f}')
