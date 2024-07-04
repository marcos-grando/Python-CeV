'''
lista = []
print('Digite quantos números você quiser!')
print('"999" e veja a média e o "maior>menor"')
add = int(input('Número: '))
lista.append(add)
while True:
    add = input(f'{lista} mais: ')
    lista.append(add)
    if add.isnumeric()==False:
        lista.remove(add)
        print('[ERRO] Digite apenas números!')
    if add=='999':
        lista.remove(add)
        print(f'Maior Nº: {max(lista)}; Menor Nº: {min(lista)}; Média: {sum([int(x) for x in lista])/len(lista)}!')
        print('-=-'*15)
        opt = int(input('Quer adicionar mais números? [1] Sim/[2] Não: '))
        if opt==2:
            break
print('-=-=-=-Finalizado-=-=-=-')
'''
lista = []
print('Digite quantos números você quiser!')
print('"999" e veja a média e o "maior>menor"')
add = int(input('Número: '))
lista.append(add)
while True:
    add = (input(f'{lista} mais: '))
    lista.append(add)
    if add.isnumeric()==False:
        lista.remove(add)
        print('[ERRO] Digite apenas números!')
    if int(add)==999:
        lista.remove(add)
        print(f'Maior Nº: {max([int(x) for x in lista])}; Menor Nº: {min([int(x) for x in lista])}; Média: {sum([int(x) for x in lista])/len(lista)}!')
        print('-=-'*15)
        opt = int(input('Quer adicionar mais números? [1] Sim/[2] Não: '))
        if opt==2:
            break
print('-=-=-=-Finalizado-=-=-=-')