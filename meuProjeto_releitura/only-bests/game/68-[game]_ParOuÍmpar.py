from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.defsGood_mdl.defsGood import *
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from random import randint
from time import sleep

numsMachine = []
winMachine = winPlayer = 0
while True:
    head_timeTitle(bold_('+', 8)+bold_('-'*8, 4)+bold_('[ Par ou Ímpar ]', 8)+bold_('-'*8, 4)+bold_('+', 8), True, 0.02)

    print(bold_('| ', 8), end='')
    head_timeTitle(bold_('-'*10, 4), False)
    print(' '*20, bold_('|', 8))

    print(bold_('| ', 8), end='')
    head_timeTitle(f'[{bold_('1', 6)}] {bold_('Ímpar', 8)}', False)
    print(' '*21, bold_('|', 8))

    print(bold_('| ', 8), end='')
    head_timeTitle(f'[{bold_('2', 6)}] {bold_('Par', 8)}', False)
    print(' '*23, bold_('|', 8))

    print(bold_('+', 8), end='')
    head_timeTitle(bold_('-'*32, 4), False, 0.02)
    print(bold_('+', 8))

    numMachine = randint(0,10)
    while numMachine in numsMachine:
        numMachine = randint(0,10)
    numsMachine.append(numMachine)
    if len(numsMachine)==5:
        numsMachine.clear()

    head_timeTitle(f'{bold_('Par/ímpar', 8)}', False)
    parimpar = str(input(f' [{cor_bold(6)}')).lower().strip()
    cor_bold()
    while parimpar not in('par', 'pares', 'impar', 'ímpar', 'impares', 'ímpares', '1', '2', 'um', 'dois'):
        head_timeTitle(f'{bold_('Par/ímpar', 8)}', False)
        parimpar = str(input(f' [{cor_bold(6)}')).lower().strip()
        cor_bold()

    head_timeTitle(f'{neutro_('Numº 0~10', 8)}', False)
    numPlayer = str(input(f' [{cor_bold(6)}')).lower().strip()
    cor_bold()
    while numPlayer not in('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        head_timeTitle(f'{bold_('Nº 0~10', 8)}', False)
        numPlayer = str(input(f' [{cor_bold(6)}')).lower().strip()
        cor_bold()
    numPlayer = int(numPlayer)

    loading_tx(False, '1..', 1, 5, 1, 0.3)
    loading_tx(False, '2..', 1, 5, 1, 0.3)
    loading_tx(False, '3..', 1, 5, 1, 0.3)

    head_timeTitle(bold_('+', 8)+bold_('-'*11, 4)+bold_('[ FIGTH! ]', 8)+bold_('-'*11, 4)+bold_('+', 8), True, 0.02)

    head_timeTitle(bold_('| ', 8)+f'{f'[{bold_('Player', 2)}]: {bold_(f'{numPlayer}', 4)} {bold_('VS', 8)} {bold_(f'{numMachine}', 4)} :[{bold_('Machine', 1)}]':^81}', False, 0.035)
    print(f'{bold_('|', 8):>0}')

    if (numMachine+numPlayer)%2==0:
        if parimpar in('par','pares','2','dois'):
            print(bold_('| ', 8)+' '*6, end='')
            head_timeTitle(f'{f'{bold_('>>> ', 2)}{bold_(numMachine+numPlayer, 6)} {bold_('é par', 8)}{bold_(' <<<', 2)}':^58}', False)
            print(bold_(' '*7+'|', 8))

            print(bold_('|', 8)+' '*9, end='')
            head_timeTitle(f'{f'{bold_('Player venceu', 2)}':^24}', False)
            print(bold_(' '*9+'|', 8))
            winPlayer+=1
        else:
            print(bold_('| ', 8)+' '*6, end='')
            head_timeTitle(f'{f'{bold_('>>> ', 1)}{bold_(numMachine+numPlayer, 6)} {bold_('é par', 8)}{bold_(' <<<', 1)}':^58}', False)
            print(bold_(' '*7+'|', 8))

            print(bold_('|', 8)+' '*9, end='')
            head_timeTitle(f'{f'{bold_('Máquina venceu', 1)}':^24}', False)
            print(bold_(' '*9+'|', 8))
            winMachine+=1
    else:
        if parimpar in('impar','impares','ímpar','ímpares','1','um'):
            print(bold_('| ', 8)+' '*5, end='')
            head_timeTitle(f'{f'{bold_('>>> ', 2)}{bold_(numMachine+numPlayer, 6)} {bold_('é ímpar', 8)}{bold_(' <<<', 2)}':^60}', False)
            print(bold_(' '*6+'|', 8))

            print(bold_('|', 8)+' '*9, end='')
            head_timeTitle(f'{f'{bold_('Player venceu', 2)}':^24}', False)
            print(bold_(' '*9+'|', 8))
            winPlayer+=1
        else:
            print(bold_('| ', 8)+' '*5, end='')
            head_timeTitle(f'{f'{bold_('>>> ', 1)}{bold_(numMachine+numPlayer, 6)} {bold_('é ímpar', 8)}{bold_(' <<<', 1)}':^60}', False)
            print(bold_(' '*6+'|', 8))

            print(bold_('|', 8)+' '*9, end='')
            head_timeTitle(f'{f'{bold_('Máquina venceu', 1)}':^24}', False)
            print(bold_(' '*9+'|', 8))
            winMachine+=1
    
    print(bold_('+', 8), end='')
    head_timeTitle(bold_('-'*32, 4), False, 0.02)
    print(bold_('+', 8))

    head_timeTitle(bold_('Jogar.. mais?', 8), False, 0.2)
    fim = str(input(' ')).lower().strip()
    while fim not in ('sim','si','ss','s','yes','jogar','quero','não','no','nn','n','não jogar','n jogar','n quero','não quero'):
        print(bold_('[', 4)+'Apenas digite se quer ou não jogar mais'+bold_(']', 4))
        head_timeTitle(bold_('Quer jogar mais?', 4), False, 0.07)
        fim = str(input(' ')).lower().strip()
    if fim in ('não','no','nn','n','não jogar','n jogar','n quero','não quero'):
        break

print(bold_('+', 8), end='')
head_timeTitle(bold_('-'*32, 4), False, 0.02)
print(bold_('+', 8))

partidas = winMachine+winPlayer

head_timeTitle(f'Foram {partidas} confrontos')
if winPlayer>winMachine:
    head_timeTitle(f'O jogador venceu a máquina')
    head_timeTitle(f'{winPlayer} vitória(s) e {winMachine} derrota(s)')
elif winMachine>winPlayer:
    head_timeTitle(f'A máquina venceu o jogador')
    head_timeTitle(f'{winMachine} vitória(s) e {winPlayer} derrota(s)')
elif winPlayer==winMachine:
    head_timeTitle(f'Houve um indiscutível empate')
    head_timeTitle(f'Ambos lados venceram {int(partidas/2)} vezes')

print(bold_('+', 8), end='')
head_timeTitle(bold_('-'*32, 4), False, 0.02)
print(bold_('+', 8))
