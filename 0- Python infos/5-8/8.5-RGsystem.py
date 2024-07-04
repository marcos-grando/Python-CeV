'''
==============================================================

Att mais recente:

Além de eu não ter tido sucesso em 100% do que eu queria fazer,
percebi mais recentemente, enquanto aprendo MySQL, que minha ideia
era na verdade a criação de algo parecido com uma "chave primária".

Claro, guardado às proporções. 

Ainda assim, deixarei registrado aqui como uma brincadeira dos meus 
primeiros aprendizados com programação num geral. 

Ou seja, todos os arquivos 8- ou 8.5- são inúteis e desnecessários.

==============================================================
'''











'''Sistema de RG é útil para COMPARAÇÃO, ou seja (if X != Y), 
sendo TODOS os dados de X iguais os de Y, teríamos X != Y -> False; 
Inserindo um código de ID nesses dados, teríamos X != Y -> True. '''


#[nome, idade, rg]
dados = [['Marcos', 15, 0], ['Fiona', 14, 1], ['Maria', 11, 2], ['Marcos', 15, 3]]
ordAlf = sorted(dados)

for dd in ordAlf:
    print(f'{dd[0]} tem {dd[1]} anos, foi o {dd[2]+1}º registro feito.')
# Dessa forma, consigo ter RG como uma info sobre os mais jovens e velhos registros.
# Nesse for acima, dd já se refere às mini-listas presente em ordAlf (a lista maior).
# Por isso, apenas dd[] já traz o dado necessário. Não precisando ser dd[][].


# No caso abaixo, o 'RG' é a própria colocação dos times
times = (['botafogo', 1], ['Atlético-MG', 2], ['Bragantino', 3], ['Atlético-PR', 4], ['Bahia', 5], ['Internacional', 6], ['Crcuzeiro', 7], ['Flamengo', 8],
        ['Grêmio', 9], ['Criciúma', 10], ['Fortaleza', 11], ['Palmeiras', 12], ['Juventude', 13], ['São Paulo', 14], ['Corinthians', 15],
        ['Fluminense', 16], ['Vasco da Gama', 17], ['Vitória', 18], ['Atlético-GO', 19], ['Cuiabá', 20])
alfTimes = sorted(times)

for timesNO in alfTimes:
        print(f'{timesNO[0]:<14} {timesNO[1]:>2}º colocado; ')




'''
daods = []
dados.append(['Marcos', 15, 0])
dados.append(['Fiona', 14, 1])
dados.append(['Maria', 11, 2])
#   ou 

dados = []
rg=0
while True: #[stop]
    nome = str(input('Nome: '))
    if nome=='stop':
        break
    idade = int(input('Idade: '))
    dados.append([nome, idade, rg])
    rg+=1
'''
'''for c in range(0,20):
    print(f'{ordAlf[c]} em {dados.index(ordAlf[c])+1}')'''