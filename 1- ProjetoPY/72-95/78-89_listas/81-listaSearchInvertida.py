lista = []
lisPo = []
c=0
while True:
    num = int(input(f'{c+1}º número: '))
    lista.append(num)
    if num==5:
        lisPo.append(c)
    if lista[-1]==999:
        del lista[-1]
        print(f'Total: {len(lista)}.')
        if 5 in lista:
            if len(lisPo)==1:
                print(f'5 na {lisPo[0]}º posição!')
            elif len(lisPo)==2:
                print('5 nas posições: ', end='')
                for lp in range(0,len(lisPo)):
                    if lisPo[lp]!=lisPo[-1]:
                        print(f'{lisPo[lp]+1}º ', end='')
                    elif lisPo[lp]==lisPo[-1]:
                        print(f'e {lisPo[lp]+1}º !')
            elif len(lisPo)>=3:
                print('5 nas posições: ', end='')
                for lp in range(0,len(lisPo)):
                    if lisPo[lp]!=lisPo[-1] and lisPo[lp]!=lisPo[-2]:
                        print(f'{lisPo[lp]+1}º, ', end='')
                    elif lisPo[lp]==lisPo[-2]:
                        print(f'{lisPo[lp]+1}º ', end='')
                    elif lisPo[lp]==lisPo[-1]:
                        print(f'e {lisPo[lp]+1}º !')
        else:
            print('Você não digitou 5 !')
        print(sorted(lista, reverse=True))
        break
    c+=1

'''
    for lp in range(0, len(lista)):   
        if lista[lp]==5:
            lisPo.append(lp)
'''