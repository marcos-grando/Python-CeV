from random import randint
def format(list):
    for elements in list:
        if elements!=list[-1] and elements!=list[-2]:
            print(f'{elements},', end=' ')
        elif elements==list[-2]:
            print(f'{elements}', end=' ')
        elif elements==list[-1]:
            print(f'e {elements}.')
def sorteio(listaSorteada, alcance):
    while len(listaSorteada)!=5:
        sort = randint(0, alcance)
        while sort in listaSorteada:
            sort = randint(0, alcance)
        listaSorteada.append(sort)
def somaPar(listaPares, listaPrincipal):
    for par in listaPrincipal:
        if par%2==0:
            listaPares.append(par)

ns = int(input('Nºs de 0 à: '))

print(f'-='*25)
listaSort = []
sorteio(listaSort, ns)
print(f'Os números sorteados foram:', end=' ')
format(listaSort)
print(f'-='*19)

print(f'-='*19)
listaPar = []
somaPar(listaPar, listaSort)
if len(listaPar)==0:
    print('Sem números pares.')
elif len(listaPar)==1:
    print(f'{listaPar[0]} é o único número par.')
elif len(listaPar)>=2:
    print(f'Os números pares são:', end=' ')
    format(listaPar)
    print(f'Soma dos pares dá >> {sum(listaPar)} <<')
print(f'-='*25)
