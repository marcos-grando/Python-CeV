pessoas = int(input('Grupo tem quantas pessoas? '))
nomes = []
idades = []
sexos = []
media = 0
for a in range(0, pessoas):
    print(f'-=--=-{a+1}ª PESSOA-=--=-')
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))
    sexos.append(str(input('Sexo [F/M]: ')).lower())
    media += idades[a]

print('-=-'*16)
print(f'O grupo tem uma idade média de {media/pessoas:.0f} anos.')

# {-----Pessoa mais velha-----}        
maxIdadeLista = []
maxNomesLista = []   
maxIdade = max(idades)              #Retorna a 'primeira' maior idade
maxLista = idades.index(maxIdade)   #Retorna a casa dessa idade na lista 
cont = 0                
for b in range(0, pessoas):
    if idades[b]==maxIdade:
        maxIdadeLista.append(idades[b])
        maxNomesLista.append(nomes[b])
        cont += 1
print('-=-'*16)
if cont==1:
    print(f'A pessoa mais velha do grupo é {nomes[maxLista]} com {idades[maxLista]} anos!')
elif cont>1:
    print(f'Temos {cont} pessoas como as mais velhas do grupo:')
    for d in range(0, cont):    
        if sexos[b]=='f':
            print(f'Srª {maxNomesLista[d]} com {maxIdadeLista[d]} anos.')
        elif sexos[b]=='m':
            print(f'Srº {maxNomesLista[d]} com {maxIdadeLista[d]} anos.')

# {-----Mulheres<20-----}
listaNomesMul = []
ListaIdadeMul = []
cont1 = 0
for c in range(0, pessoas):
    if idades[c]<20 and sexos[c]=='f':
        listaNomesMul.append(nomes[c])
        ListaIdadeMul.append(idades[c])
        cont1 += 1
print('-=-'*16)
if cont1==1:
    print(f'Abaixo de 20 anos temos apenas a {nomes[c]} com {idades[c]} anos!')
elif cont1>=2:
    print(f'Mulheres com menos de 20 anos temos {cont1} pessoas: ')
    for e in range(0, cont1):
        print(f'{listaNomesMul[e]} com {ListaIdadeMul[e]} anos')



'''
'Damiona', 'João', 'Maria', 'Cristóvan', 'Nana', 'Marcos', 'Sara'
75, 65, 48, 75, 12, 18, 17
'f', 'm', 'f', 'm', 'f', 'm', 'f'
'a', 'b', 'c', 'd', 'd', 'd', 'd'
0, 1, 2, 3, 4, 5, 6
'''  