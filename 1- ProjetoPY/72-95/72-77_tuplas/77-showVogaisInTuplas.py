tupla = ('abacaxi', 'carai', 'eita preula', 'abracadabra', 'showdebola', 'madonnashow')

#""minha"" versão
vogal = 'aeiouAEIOU'
for palavra in tupla:
    print(f'{palavra} = ', end='')
    print(''.join(vog for vog in palavra if vog in vogal))


#v com ref da aula

for palavra in tupla:
    print(f'\n{palavra} = ', end='')
    for vog in palavra:
        if vog in 'aeiouAEIOU':
            print(vog, end='')
