listas = []

listas.insert(0, [107, 'A', 0])
listas.insert(1, [53, 'B', 1])
listas.insert(2, [5, 'C', 2])
listas.append([3, 'D', 3])
listas.insert(3, [6, 'E', 4])
listas.append([107, 'R', 5])
listas.append([3, 'G', 6])

print(f'Os {len(listas)} cadastrados são: ')
for c in range(0, len(listas)):
    if listas[c][2]!=listas[-1][2]:
        print(f'{listas[c][1]}, com {listas[c][0]}kg;')
    elif listas[c][2]==listas[-1][2]:
        print(f'E {listas[c][1]}, com {listas[c][0]}kg.')
print('-='*11)

leves = []
pesos = []
for n in range(0,len(listas)):
    if listas[n][0]==listas[listas.index(max(listas))][0]:
        pesos.append(listas[n])
    if listas[n][0]==listas[listas.index(min(listas))][0]:
        leves.append(listas[n])

print(f'--'*11)
if len(pesos)==1:
    print(f'{pesos[0][1]} com {pesos[0][0]}kg é a pessoas mais pesada do grupo!')
elif len(pesos)==2:
    print(f'Com {pesos[0][0]}kg, {pesos[0][1]} e {pesos[-1][1]} são as pessoas mais pesadas do grupo!')
elif len(pesos)>=3:
    print(f'Os {len(pesos)} mais pesados são: ')
    for p in range(0, len(pesos)):
        if pesos[p][2]!=pesos[-1][2]:
            print(f'{pesos[p][1]}, com {pesos[p][0]}kg;')
        elif pesos[p][2]==pesos[-1][2]:
            print(f'E {pesos[p][1]}, com {pesos[p][0]}kg.')
print(f'--'*11)

print(f'--'*11)
if len(leves)==1:
    print(f'{leves[0][1]} com {leves[0][0]}kg é a pessoa mais leve do grupo!')
elif len(leves)==2:
    print(f'Com {leves[0][0]}kg, {leves[0][1]} e {leves[-1][1]} são as pessoas mais leves do grupo!')
elif len(leves)>=3:
    print(f'Os {len(leves)} mais leves são: ')
    for p in range(0, len(leves)):
        if leves[p][2]!=leves[-1][2]:
            print(f'{leves[p][1]}, com {leves[p][0]}kg;')
        elif leves[p][2]==leves[-1][2]:
            print(f'E {leves[p][1]}, com {leves[p][0]}kg.') 
print(f'--'*11)


'''if listas[n][0]==listas[listas.index(max(listas))][0]:'''


