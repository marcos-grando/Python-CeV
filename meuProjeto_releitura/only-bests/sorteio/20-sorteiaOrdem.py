from random import sample, choice, randint

def random_ordemNomes():
    print('Escreva abaixo uma lista de nomes para sorteio. ["parar" para finalizar]')
    lista = []
    c=0
    while True:
        c+=1
        nome = str(input(f'{c}º nome: '))
        if nome.lower()=='parar':
            break
        else:
            lista.append(nome)
    listaSorteada = sample(lista, len(lista))
    print('-'*27)
    print(f'{f'A ordem de apresentação':^27}')
    print('-'*27)
    for n, nomes in enumerate(listaSorteada):
        print(f'{f'{n+1}º lugar:':<15}', end='')
        print(f'{nomes}')

def random_ordemItens():
    print('Escreva abaixo uma lista dos itens para sorteio. ["parar" para finalizar]')
    lista = []
    c=0
    while True:
        c+=1
        item = input(f'{c}º item: ')
        if item.lower()=='parar':
            break
        else: 
            lista.append(item)
    listaSorteada = sample(lista, len(lista))
    print('-'*27)
    print(f'{'Ordem do sorteio':^27}')
    print('-'*27)
    for n, itens in enumerate(listaSorteada):
        print(f'{f'{n+1}º lugar:':<15}', end='')
        print(f'{itens}')

def random_sorteio():
    print('-'*27)
    print(f'{'[ SORTEIAÇÃO ]':=^27}')
    print('-'*27, f'\n{"'parar'p/ encerrar":^27}\n')
    lista = []
    c=0
    while True:
        c+=1
        competidor = input(f'{c}º competidor: ')
        if competidor.lower()=='parar':
            break
        else:
            lista.append(competidor)
    vencedorSorteio = choice(lista)
    print('-'*27)
    print(f'Total de competidores: {len(lista)}')
    print(f'O vencedor foi...')
    print(f'{f'[ {vencedorSorteio} ]':=^27}')
    print('-'*27)

def random_sorteioValores(quantidade=5, valorAté=20):
    lista = []
    if quantidade>valorAté:
        print('------------------------------------------------------------')
        print('[ERRO] Não haverá número repetido no sorteio.')
        print('Portanto, a *quantidade* de números sorteados ')
        print('deve ser maior que o *valorAté* para sorteio.')
        print('------------------------------------------------------------')
    else:
        while len(lista)!=quantidade:
            sorteio = randint(0,valorAté)
            while sorteio in lista:
                sorteio = randint(0,valorAté)
            lista.append(sorteio)
        else:
            print(f'Valores sorteados: ', end='')
            for n in range(0, len(lista)-1):
                print(f'{lista[n]}, ' if lista[n]!=lista[-2] else f'{lista[n]} e ', end='')
            print(f'{lista[-1]}.')

# engloba exc19/20/74

#random_ordemNomes()
#random_ordemItens()

#random_sorteio()

#random_sorteioValores(quantidade=3, valorAté=15)