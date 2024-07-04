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












#com sistema de RG: ['nome', RG]     ===     'RG' sempre único, dados pessoas podem ser repetidos!

lista = [['pessoa A', 0],['pessoa B', 1],['pessoa C', 2],['pessoa D', 3],['pessoa E', 4]]

if len(lista)==1:
    print(f'Temos apenas 1 pessoa cadastrada:')
    print(f'{lista[0][0]}.')

elif len(lista)==2:
    print(f'Temos 2 pessoas cadastradas:')
    for lp in range(0,len(lista)):
        if lista[lp][1]!=lista[-1][1]:
            print(f'{lista[lp][0]} e', end=' ')
        elif lista[lp][1]==lista[-1][1]:
            print(f'{lista[lp][0]}.')

#    OR  ==  Formatação mais simples:
#elif len(lista)==2:
#    print(f'Temos 2 pessoas cadastradas: {lista[0][0]} e {lista[1][0]} !')

elif len(lista)>=3:
    for lp in range(0,len(lista)):
        if lista[lp][1]!=lista[-1][1] and lista[lp][1]!=lista[-2][1]:
            print(f'{lista[lp][0]},', end=' ')
        elif lista[lp][1]==lista[-2][1]:
            print(f'{lista[lp][0]} e', end=' ')
        elif lista[lp][1]==lista[-1][1]:
            print(f'{lista[lp][0]}.')

#    OR  ==  Formatação mais bruta, mas funciona:
#elif len(lista)>=3:
#    print(f'Temos {len(lista)} pessoas cadastradas:')
#    for lp in range(0,len(lista)):
#        if lista[lp][1]!=lista[-1][1]:
#            print(f'{lista[lp][0]};')
#        elif lista[lp][1]==lista[-1][1]:
#            print(f'E {lista[lp][0]}.') 

'''
lista = ['a', 'b', 'c', 'd', 'e']

if len(lista)==1:
    print(f'Temos apenas 1 pessoa cadastrada:')
    print(f'{lista[0]}.')

elif len(lista)==2:
    print(f'Temos 2 pessoas cadastradas:')
    for lp in range(0,len(lista)):
        if lista[lp]!=lista[-1]:
            print(f'{lista[lp]} ', end='')
        elif lista[lp]==lista[-1]:
            print(f'e {lista[lp]}.')

elif len(lista)>=3:
    for lp in range(0,len(lista)):
        if lista[lp]!=lista[-1] and lista[lp]!=lista[-2]:
            print(f'{lista[lp]}, ', end='')
        elif lista[lp]==lista[-2]:
            print(f'{lista[lp]} ')
        elif lista[lp]==lista[-1]:
            print(f'e {lista[lp]}.')
'''