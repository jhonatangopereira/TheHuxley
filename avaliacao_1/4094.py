p1 = int(input())
p2 = int(input())
p3 = int(input())

if 1<=p1<=100 and 1<=p2<=100 and 1<=p3<=100:
    if p1==p2==p3:
        print('3 trofeus e 0 placa')
    elif p1!=p2!=p3:
        print('1 trofeu e 1 placa')
    elif p1==p2:
        if p1>p3:
            print('2 trofeus e 1 placa')
        elif p3>p1:
            print('1 trofeu e 2 placas')
    elif p2==p3:
        if p1>p2:
            print('1 trofeu e 2 placas')
        elif p2>p1:
            print('2 trofeus e 1 placa')
    elif p1==p3:
        if p1>p2:
            print('2 trofeus e 1 placa')
        elif p2>p1:
            print('1 trofeu e 2 placas')
else:
    print('Violacao das restricoes')
