lista = []
#lista = [[3,2,9],[4,5,7],[6,2,5]]

for m in range(0,3):
    lista.append([])
    for mm in range(0,3):
        num = int(input(f'Valor para [{m}, {mm}]: '))
        lista[m].append(num)

lista1 = [[],[]] # coluns = pares = 0
for p in range(0,3):
    for pp in range(0,3):
        if lista[p][pp]%2==0:
            lista1[0].append(lista[p][pp]) # pares += lista[p][pp]
        if lista[p][pp]==lista[p][2]:
            lista1[1].append(lista[p][2]) # coluns += lista[p][pp]

print('-='*17)
for p in range(0,3):
    for pp in range(0,3):
        print(f'[{lista[p][pp]:^5}] ', end='')
    print('')
print('-='*17)
print(f'Soma de todos pares: {sum(lista1[0])};')
print(f'Soma da 3 coluna: {sum(lista1[1])};')
print(f'Maior valor segunda linha: {max(lista[1])}.')
print('-='*17)

'''
matriz = str(input('Nova matriz? [s/n]')).lower().strip()
if matriz in ('s', 'sim', 'yes', 'si'):
    for newm in range(0,9):
    
print(lista[0][0],lista[0][1],lista[0][2])
print(lista[1][0],lista[1][1],lista[1][2])
print(lista[2][0],lista[2][1],lista[2][2])
'''