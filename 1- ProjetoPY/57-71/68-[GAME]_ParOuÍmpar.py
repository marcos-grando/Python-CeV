from random import randint
from time import sleep

cont = 0
print('Player vs Machine! ')
while True:
    parimpar = str(input('Par ou ímpar? ')).strip().lower()
    while parimpar not in('par', 'ímpar', 'impar'):
        parimpar = str(input('[ERRO] Palavra não reconhecida!\nPar ou ímpar? ')).strip().lower()  
    print('-=-'*12)  

    sleep(1)
    print(f'[Player]: {parimpar.upper()} VS ', end='')
    print('PAR :[Machine]' if parimpar=='ímpar' or parimpar=='impar' else 'ÍMPAR :[Machine]')
    print('-=-'*12)

    numPlayer = int(input('Escolha um número de 0 à 10: '))
    numIA = randint(0, 10)
    sleep(1)
    print(f'Player jogou {numPlayer} & Machine jogou {numIA} !')
    print(f'Resultado >> {numIA+numPlayer} << Número ', end='')
    if (numIA+numPlayer)%2==0 and parimpar in ('par', 'pares') or (numIA+numPlayer)%2!=0 and parimpar in ('ímpar', 'impar', 'ímpares', 'impares'):
        print('PAR!\n   -=--=-[ Player WIN ]-=--=-' if (numIA+numPlayer)%2==0 else 'ÍMPAR!\n   -=--=-[ Player WIN ]-=--=-')
        print('-=-'*12)
    else:
        print('PAR!\n   -=--=-[ Machine WIN ]-=--=-' if (numIA+numPlayer)%2==0 else 'ÍMPAR!\n   -=--=-[ Machine WIN ]-=--=-')
        print('-=-'*12)        
        sleep(1)
        print(f'Você venceu {cont}x seguidas!')
        break
    cont += 1
    
