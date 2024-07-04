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











# [nome, idade, rg]
dados = [['Marcos', 15, 0], ['Fiona', 14, 1], ['Maria', 11, 2], ['Marcos', 15, 3], ['Jusé', 15, 4]]
ordAlf = sorted(dados)
dadosS = []
for ss in dados:
    dadosS.append(ss[1])
print(dadosS)
max = max(dadosS)

for dv in dados:
    if dv[1]==max:
        print(f'{dv[0]}; ')

'''
for dadosOrdenados in ordAlf:
    for dd in dados:
        if dadosOrdenados==dd:
            print(f'{dd[0]} tem {dd[1]} anos.')

# Nesse 'for' acima, 'dd' já se refere às mini-listas presente em ordAlf (a lista maior).
#Essa lógica acima usa um cruzamento de dados, nesse caso não é necessário;
#Mas em casos de cruzamento de listas DIFERENTES essa lógica é útil.



# No caso abaixo, o 'RG' é a própria colocação dos times
times = (['botafogo', 1], ['Atlético-MG', 2], ['Bragantino', 3], ['Atlético-PR', 4], ['Bahia', 5], ['Internacional', 6], ['Crcuzeiro', 7], ['Flamengo', 8],
        ['Grêmio', 9], ['Criciúma', 10], ['Fortaleza', 11], ['Palmeiras', 12], ['Juventude', 13], ['São Paulo', 14], ['Corinthians', 15],
        ['Fluminense', 16], ['Vasco da Gama', 17], ['Vitória', 18], ['Atlético-GO', 19], ['Cuiabá', 20])
alfTimes = sorted(times)

for timesO in alfTimes:
    for timesNO in times:
        if timesO==timesNO:
            print(f'{timesNO[0]:<14} {timesNO[1]:>2}º colocado; ')
'''