from random import randint
from time import sleep

colors = {'limpar':'\033[m', 'vermelho':'\033[31m', 'ciano':'\033[36m', 'verde':'\033[32m', 'roxo':'\033[35m', 'azul':'\033[34m', 'cinza':'\033[37m'}

print(f'{colors['verde']}Player {colors['ciano']}vs {colors['vermelho']}Machine! {colors['limpar']}')
while True:
    parimpar = str(input(f'{colors['cinza']}Par ou ímpar? {colors['verde']}')).strip().lower()
    while parimpar not in('par', 'ímpar', 'impar'):
        parimpar = str(input(f'{colors['vermelho']}[ERRO] {colors['cinza']}Palavra não reconhecida!\n{colors['ciano']}Par ou ímpar? {colors['verde']}Escolha: ')).strip().lower()  
    print(f'{colors['cinza']}-=-{colors['limpar']}'*12)  

    sleep(1)
    print(f'{colors['verde']}[Player]: {parimpar.upper()} {colors['ciano']}VS {colors['vermelho']}', end='')
    print('PAR :[Machine]' if parimpar=='ímpar' or parimpar=='impar' else 'ÍMPAR :[Machine]')
    print(f'{colors['cinza']}-=-{colors['limpar']}'*12)  

    numPlayer = int(input(f'{colors['cinza']}Escolha um número de 0 à 10: {colors['verde']}'))
    numIA = randint(0, 10)

    print(f'{colors['verde']}Player jogou {numPlayer} {colors['ciano']}& {colors['vermelho']}Machine jogou {numIA} !')
    print(f'{colors['azul']}Resultado >> {numIA+numPlayer} << Número ', end='')
    if (numIA+numPlayer)%2==0 and parimpar in ('par', 'pares') or (numIA+numPlayer)%2!=0 and parimpar in ('ímpar', 'impar', 'ímpares', 'impares'):
        print(f'PAR!\n   {colors['verde']}-=--=-[ Player WIN ]-=--=-' if (numIA+numPlayer)%2==0 else f'ÍMPAR!\n   {colors['verde']}-=--=-[ Player WIN ]-=--=-')
    else:
        print(f'PAR!\n   {colors['vermelho']}-=--=-[ Machine WIN ]-=--=-' if (numIA+numPlayer)%2==0 else f'ÍMPAR!\n   {colors['vermelho']}-=--=-[ Machine WIN ]-=--=-')
    print(f'{colors['cinza']}-=-{colors['limpar']}'*12)  
