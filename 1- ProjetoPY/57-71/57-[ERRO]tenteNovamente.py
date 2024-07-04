#Prof versão (bem mais eficiente)
sexo = str(input('Sexo [F/M]: ')).strip().lower()[0]
while sexo not in 'MmFf':
    print('[ERRO] Novamente, informe seu sexo [F/M]: ').strip().lower()[0]
print('Dados registrados com sucesso!')


#Minha versão (menos eficiente)
'''
while True:
    sexo = str(input('Sexo [f/m]: ')).strip().lower()[0]
    if sexo=='f' or sexo=='m':
        print('Ok!')
        break
    if sexo!='f' or sexo!='m':
        print('[ERRO] Tente novamente.')
'''

#Erro com lista OBS: necessário macete {...([int(x) for x in lista])}
'''
lista = []
print('Digite quantos números você quiser! ["999" para finalizar]')
add = int(input('Número: '))
lista.append(add)
while True:
    add = input(f'{lista} mais: ')
    lista.append(add)
    if add.isnumeric()==False: #Retorna False se digitado não for número
        lista.remove(add)      #Dessa forma, se for digitado uma letra, vai remover
        print('[ERRO] Digite apenas números!')
    elif add=='999':
        lista.remove(add)
        print(f'A soma dos {len(lista)} números que você digitou resulta no valor de {sum([int(x) for x in lista])}.')
        break
print('-=-=-=-Finalizado-=-=-=-')
'''