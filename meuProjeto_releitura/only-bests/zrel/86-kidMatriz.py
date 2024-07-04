lista = []
#lista = [[3,2,9],[4,5,7],[6,2,5]]

#Busca e armeneza os dados
for m in range(0,4):
    lista.append([]) #não necessário se usar opção de variável abaixo
    for mm in range(0,4):
        lista[m].append(int(input(f'Valor para [{m}, {mm}]: ')))
        #lista[m][mm] = ([int(input(f'Valor para [{m}, {mm}]: '))])

#Printa/mostra os dados
'''
for p in range(0,3):
    for pp in range(0,3):
        print(f'[{lista[p][pp]:^5}] ', end='')
    print('')
'''
for linha in lista:
    for coluna in linha:
        print(f'[{coluna:^5}]', end='')
    print('')