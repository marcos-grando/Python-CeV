lista = []

print('Digite números [999=parar]')
while True:
    newNum = int(input('Digite número: '))
    if newNum==999:
        break
    if newNum not in lista:
        lista.append(newNum)
        print(f'{newNum} adicionado! ')
    elif newNum in lista:
        print(f'[ERRO] {newNum} já existe!')
'''
for r in range(0, len(lista)):
    while lista.count(lista[r])>1:
        lista.remove(lista[r])
'''

print(sorted(lista))
