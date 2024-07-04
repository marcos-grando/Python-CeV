from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.defsGood_mdl.defsGood import *
from mydefs_package.mycores_mdl.mycores import *
from random import choice, randint
from time import sleep
xFormat = len('[ JO-KÊN-PO ]')
lista = ['pedra', 'papel', 'tesoura']

print(' '*5, end='')
arrasta_pLadoTxt('[ JO-KÊN-PO ]', True, 7, 4, 4, 1, 0.035)
head_timeTitle(' '*11+'-'*xFormat)

for enum, opt in enumerate(lista):
    head_timeTitle(f'{f' [{bold_(enum+1, 6)}] {undl_(opt.title(), 7)}':^54}', True, 0.020)
print('     ', end='')
head_timeTitle('Jogue:', end='')
option = readn_cleanNum(f' [{cor_bold(6)}')

while option>3:
    head_timeTitle(cor_bold()+' '*11+'-'*xFormat)
    head_timeTitle(f'[{bold_('ERRO', 1)}] {undl_('Jogada inválida!', 3)}')
    head_timeTitle(' '*11+'-'*xFormat)
    option = readn_cleanNum(f'    Jogue: [{cor_bold(6)}')
print(cor_bold(), end='           ')
loading_(2, 3, 4, 1)

head_timeTitle('-'*xFormat)
print(' '*7, end='')
arrasta_pLadoTxt('[  GO!  ]', True, 7, 4, 4, 1, 0.035)

print(' '*13, end='')
head_timeTitle(bold_('JO-',1), False)
sleep(0.5)
head_timeTitle(bold_('KEN',2), False)
sleep(0.5)
head_timeTitle(bold_('-PÔ', 6), True)

sorteio = randint(0, 2)
if option==3 or option==1 or option==2:
    head_timeTitle(f'{f'{neutro_('Máquina', 1)} {lista[sorteio].upper()} {bold_('V', 1)}{bold_('S', 2)} {lista[option-1].upper()} {neutro_('Player', 2)}':^74}')
    if option-1==sorteio:
        head_timeTitle(f'{f'{undl_('EMPATE!', 3)}':^46}')
    elif option==1 and sorteio==2 or option==2 and sorteio==0 or option==3 and sorteio==1:
        head_timeTitle(f'{f'{undl_('Parabéns! Você venceu!', 2)}':^46}')
    else:
        head_timeTitle(f'{f'{undl_('GAMEOVER! Você perdeu!', 1)}':^46}')
else:
    print('[ERRO] Digite uma jogada válida!')
print(f'{f'{neutro_('-=-'*10, 4)}':^44}')

