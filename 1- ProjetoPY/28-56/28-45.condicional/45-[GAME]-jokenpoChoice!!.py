from random import choice, randint
from time import sleep

lista = ['pedra', 'papel', 'tesoura']
sorteio = choice(lista)
print('-=-'*10)
print('JO-KEN-PÔ!')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
option = int(input('Sua jogada: ')) 
print('-=-'*10)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if option==0 or option==1 or option==2:
    print(f'Máquina vs Player')
    print(f'{sorteio} vs {lista[option]}')
    if option==0 and sorteio==lista[0] or option==1 and sorteio==lista[1] or option==2 and sorteio==lista[2]:
        print('EMPATE!')
    elif option==0 and sorteio==lista[2] or option==1 and sorteio==lista[0] or option==2 and sorteio==lista[1]:
        print('Parabéns! Você venceu!')
    else:
        print('GAMEOVER! Você perdeu!')
else:
    print('[ERRO] Digite uma jogada válida!')