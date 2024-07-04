from random import choice, randint
from time import sleep

lista = ['pedra', 'papel', 'tesoura']
sorteio = randint(0, 2)
print('-=-'*10)
print('JO-KEN-PÔ!')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
option = int(input('Sua jogada: ')) 
print('-=-'*10)

if option==0 or option==1 or option==2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print(f'Máquina {lista[sorteio]} vs {lista[option]} Player')
    if option==sorteio:
        print('EMPATE!')
    elif option==0 and sorteio==2 or option==1 and sorteio==0 or option==2 and sorteio==1:
        print('Parabéns! Você venceu!')
    else:
        print('GAMEOVER! Você perdeu!')
else:
    print('[ERRO] Digite uma jogada válida!')
print('-=-'*10)


'''
if option==0 and sorteio==lista[0] or option==1 and sorteio==lista[1] or option==2 and sorteio==lista[2]:
    print(f'Máquina {sorteio} vs {lista[option]} Player')
    print('EMPATE!')
elif option==0 and sorteio==lista[2] or option==1 and sorteio==lista[0] or option==2 and sorteio==lista[1]:
    print(f'Máquina {sorteio} vs {lista[option]} Player')
    print('Parabéns! Você venceu!')
elif option==0 and sorteio==lista[1] or option==1 and sorteio==lista[2] or option==2 and sorteio==lista[0]:
    print(f'Máquina {sorteio} vs {lista[option]} Player')
    print('GAMEOVER! Você perdeu!')
elif option!=0 or option!=1 or option!=2:
    print('[ERRO] Digite opção válida!')
'''

'''
if option==1:
    if sorteio=='pedra':
        print(f'Máquina- {sorteio} vs Pedra -Player')
        print('EMPATE!')
    elif sorteio=='papel':
        print(f'Máquina- {sorteio} vs Pedra -Player')
        print('GAMEOVER! Você perdeu!')
    elif sorteio=='tesoura':
        print(f'Máquina- {sorteio} vs Pedra -Player')
        print('Parabéns! Você venceu!')
elif option==2:
    if sorteio=='pedra':
        print(f'Máquina- {sorteio} vs Papel -Player')
        print('Parabéns! Você venceu!')
    elif sorteio=='papel':
        print(f'Máquina- {sorteio} vs Papel -Player')
        print('EMPATE!')
    elif sorteio=='tesoura':
        print(f'Máquina- {sorteio} vs Papel -Player')
        print('GAMEOVER! Você perdeu!')
elif option==3:
    if sorteio=='pedra':
        print(f'Máquina- {sorteio} vs Tesoura -Player')
        print('GAMEOVER! Você perdeu!')
    elif sorteio=='papel':
        print(f'Máquina- {sorteio} vs Tesoura -Player')
        print('Parabéns! Você venceu!')
    elif sorteio=='tesoura':
        print(f'Máquina- {sorteio} vs Tesoura -Player')
        print('EMPATE!')
'''
