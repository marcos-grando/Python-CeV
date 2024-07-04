pessoas = []
p = media = int(0)
nomes = []
idades = []
sexos = []
stop = 's'
while True:
    print(f'\033[32m-=--=-\033[m {p+1}ª PESSOA \033[32m-=--=-\033[m')     
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))
    sexos.append(str(input('Sexo [F/M]: ')).lower())
    media+=idades[p]
    pessoas.append(p)
    stop = str(input('Mais alguém?[s/n]: ')).lower()
    if stop=='n' or stop=='não':
        break
    p += 1
print('\033[32m-=-\033[m'*8)


print('\033[35m-=-\033[m'*16)
print(f'O grupo tem um total de {p} pessoas.')
print(f'Com uma média de idade de {media/p:.0f} anos.')


# {-----Pessoa(s) mais velha(s)-----}
maxPessoasListas = []
maxIdadeLista = []
maxNomesListas = []
maxSexos = []
maxIdade = max(idades)
maxLista = idades.index(maxIdade)
cont = 0
for max in range(0, pessoas[-1]+1):
    if idades[max]==maxIdade:
        maxIdadeLista.append(idades[max])
        maxNomesListas.append(nomes[max])
        maxSexos.append(sexos[max])
        maxPessoasListas.append(cont)
        cont+=1
#print(cont, maxNomesListas, maxIdadeLista, maxPessoasListas)
maxTotal = len(maxPessoasListas)

print('\033[35m-=-\033[m'*16)
cont1 = 0
if cont==1:
    print(f'A pessoa mais velha do grupo é {nomes[maxLista]} com {idades[maxLista]} anos!')
else:
    print(f'Temos {maxTotal} pessoas como as mais velhas do grupo:')
while cont==2 or cont==3:
    if maxPessoasListas[cont1]==maxPessoasListas[-1]:
        if maxSexos[cont1]=='f':
            print(f'E a Srª {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
        elif maxSexos[cont1]=='m':
            print(f'E o Srº {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
        break
    elif maxSexos[cont1]=='f':
        print(f'Srª {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
    elif maxSexos[cont1]=='m':
        print(f'Srº {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
    cont1 += 1
while cont>=4:
    if maxPessoasListas[cont1]==maxPessoasListas[-1]:
        if maxSexos[cont1]=='f':
            print(f'E também a Srª {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
            break
        elif maxSexos[cont1]=='m':
            print(f'E também o Srº {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
            break            
    elif maxSexos[cont1]=='f':
        print(f'Srª {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
    elif maxSexos[cont1]=='m':
        print(f'Srº {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
    cont1 += 1

# {-----Pessoa(s) abaixo dos 18 anos-----}
menorTotalLista = []
menorIdadesLista = []
menorNomesLista = []
menorSexos = []
cont2 = 0
for menor in range(0, pessoas[-1]+1):
    if idades[menor]<18:
        menorIdadesLista.append(idades[menor])
        menorNomesLista.append(nomes[menor])
        menorSexos.append(sexos[menor])
        menorTotalLista.append(cont2)
        cont2 += 1
menorTotal = len(menorTotalLista)

print('\033[35m-=-\033[m'*16)
cont3 = 0
if cont2==1:
    print(f'Único menor de idade é {menorNomesLista[0]} com {menorIdadesLista[0]} anos.')
else:
    print(f'Temos {menorTotal} menores de idades no grupo:')
while cont2==2 or cont2==3:
    if menorTotalLista[cont3]==menorTotalLista[-1]:
        if menorSexos[cont3]=='f':
            print(f'E a {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos.')
        elif menorSexos[cont3]=='m':
            print(f'E o {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos.')
        break
    elif menorSexos[cont3]=='f':
        print(f'A {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos;')
    elif menorSexos[cont3]=='m':
        print(f'O {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos;')
    cont3 += 1
while cont2>=4:
    if menorTotalLista[cont3]==menorTotalLista[-1]:
        if menorSexos[cont3]=='f':
            print(f'E também a {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos.')
        elif menorSexos[cont3]=='m':
            print(f'E também o {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos.')
        break
    elif menorSexos[cont3]=='f':
        print(f'A {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos;')
    elif menorSexos[cont3]=='m':
        print(f'O {menorNomesLista[cont3]} com {menorIdadesLista[cont3]} anos;')
    cont3 += 1
print('\033[35m-=-\033[m'*16)

'''
if cont==1:
    print(f'A pessoa mais velha do grupo é {nomes[maxLista]} com {idades[maxLista]} anos!')
elif cont==2 or cont==3:
    print(f'Temos {cont} pessoas como as mais velhas do grupo:')
    while True:
        if maxPessoasListas[cont1]==maxPessoasListas[-1]:
            print(f'E {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
            break
        print(f'{maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos;')
        cont1+=1
elif cont>=4:
    print(f'Temos {cont} pessoas como as mais velhas do grupo:')
    while True:
        if maxPessoasListas[cont1]==maxPessoasListas[-1]:
            print(f'E também {maxNomesListas[cont1]} com {maxIdadeLista[cont1]} anos.')
            break
        print(f'{maxNomesListas[cont1]} com {maxNomesListas[cont1]} anos;')
        cont1+=1


pessoas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
p = media = int(0)
nomes = ['a', 'b', 'c', 'd', 'h', 'd', 'd', 'f', 't']
idades = [45, 65, 48, 75, 75, 18, 17, 75, 75]
sexos = ['f', 'm', 'f', 'm', 'f', 'm', 'f']
'''