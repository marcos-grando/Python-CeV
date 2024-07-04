'''
lista = []
print('Digite quantos números você quiser! ["999" para finalizar]')
add = int(input('Número: '))
lista.append(add)
while True:
    add = input(f'{lista} mais: ')
    lista.append(add)
    if add.isnumeric()==False:
        lista.remove(add)
        print('[ERRO] Digite apenas números!')
    elif add=='999':
        lista.remove(add)
        print(f'A soma dos {len(lista)} números que você digitou resulta no valor de {sum([int(x) for x in lista])}.')
        break
print('-=-=-=-Finalizado-=-=-=-')
'''

lista = []
print('Digite quantos números você quiser! ["999" para finalizar]')
add = int(input('Número: '))
lista.append(add)
while add!='999':
    add = input(f'{lista} mais: ')
    lista.append(add)
    if add.isnumeric()==False:
        lista.remove(add)
        print('[ERRO] Digite apenas números!')
lista.remove(add)
print(f'A soma dos {len(lista)} números que você digitou resulta no valor de {sum([int(x) for x in lista])}.')
print('-=-=-=-Finalizado-=-=-=-')
