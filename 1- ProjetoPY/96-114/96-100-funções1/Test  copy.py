from random import choice, randint

lista = []
for n in range(0,1000):
    lista.append(n)
print(choice(lista))

def sorteio(listaSorteada, listaPrincipal):
    while len(listaSorteada)!=5:
        sort = choice(listaPrincipal)
        while sort in listaSorteada:
            sort = choice(listaPrincipal)
        listaSorteada.append(sort)

x = int(input('n: '))
def sorteio(ls, lp):
    while len(ls)!=5:
        sort = randint(0, x)
        while sort in ls:
            sort = randint(0, x)
        ls.append(sort)


'''
print(randint(1,1000))
'''
'''
from time import sleep
def efeitoDigitar(txt):
    c=5
    cc=50
    for p in txt:
        print(p, end='', flush=True)
        if p==',':
            sleep(1)
        elif p==txt[c]:
            c+=5
            if c>len(txt)-6:
                c-=6
            sleep(0.2)
        elif p==txt[cc]:
            cc+=50
            if cc>len(txt)-51:
                cc-=51
            sleep(1)
        else:
            sleep(0.05)

texto = 'Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'
efeitoDigitar(texto)
'''