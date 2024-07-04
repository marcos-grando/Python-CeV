lista = []
print('Digite 5 números')
for n in range(0, 5):
    lista.append(int(input(f'{n+1}º número: ')))
print(lista)

print(f'Maior: {max(lista)} na ', end='')
for nn in range(0, 5):
    if lista[nn]==max(lista):
        print(f'{nn}º.. ', end='')
print('casa(s)')

print(f'Menor: {min(lista)} na ', end='')
for nnn in range(0, 5):
    if lista[nnn]==min(lista):
        print(f'{nnn}º.. ', end='')
print('casa(s)')

'''
listaMaior = []
listaMenor = []
for nn in range(0,5):
    if lista[nn]==max(lista):
        listaMaior.append(nn)
    if lista[nn]==min(lista):
        listaMenor.append(nn)
print(f'Maior: max(lista), posição: {listaMaior}')
print(f'Menor: min(lista), posição: {listaMenor}')
'''

