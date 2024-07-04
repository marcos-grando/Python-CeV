from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.defsGood_mdl.defsGood import *
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from random import randint
from time import sleep

xFormat=len('[ THE MACHINE is back ]')

print(bold_('='*55, 4))

head_timeTitle(f'|{bold_('=', 8)}'+bold_('-'*13, 4), False, 0.02)
head_timeTitle(f'{f'{bold_('=[', 8)} {bold_('THE MACHINE', 1)} {bold_('is back ]=', 8)}'}', False)
head_timeTitle(bold_('-'*13, 4)+f'{bold_('=', 8)}|', True, 0.02)

print(bold_('|')+' '*5, end='')
head_timeTitle(f'{f'{bold_('The Machine', 1)} está de volta ainda mais forte'}', False, 0.035)
print(' '*6+bold_('|'))
print(bold_('|')+' '*2, end='')
head_timeTitle(f'{f'{bold_('VOCÊ', 2)} terá que {undl_('adivinhar', 2)} um {undl_('número entre 1~1000', 0)}!!'}', False, 0.035)
print(' '*3+bold_('|'))

head_timeTitle('|'+bold_('=', 8)+bold_('-'*51, 4)+bold_('=', 8)+'|', True, 0.02)

print(bold_('|')+' '*3, end='')
head_timeTitle(f'{f'Chute {undl_('acima', 1)} do número misterioso? '}', False)
head_timeTitle(bold_('>> QUENTE <<', 1), False, 0.02)
print(' '*4+bold_('|'))

print(bold_('|')+' '*3, end='')
head_timeTitle(f'{f'Chute {undl_('abaixo', 6)} do número misterioso? '}', False)
head_timeTitle(bold_('>> FRIO <<', 6), False, 0.02)
print(' '*5+bold_('|'))

head_timeTitle('|'+bold_('=', 8)+bold_('-'*51, 4)+bold_('=', 8)+'|', True, 0.02)

numsMachine = []

while True:
    print(' '*1, end='')
    arrasta_pLadoTxt(f'[ {bold_('Tente Adivinhar', 8)} ]', True, 7, 4, 6, 1, 0.02)
    head_timeTitle(f' {bold_('-'*35, 4)}', True, 0.02)

    loading_tx(False,'>', 3, 3, 1, 0.35)

    numMach = randint(1,1000)
    while numMach in numsMachine:
        numMach = randint(1,1000)
    if numMach not in numsMachine:
        numsMachine.append(numMach)
    t=1

    head_timeTitle(bold_(f' {t}º chute:', 8), False)
    chute = readn_cleanNum(f' {cor_nat(4)}')
    print(cor_nat(), end=' ')
    loading_tx(False,'>', 3, 3, 1, 0.35)
    while True:
        if chute!=numMach:
            if chute>0 and chute<=1000:
                if chute>numMach:
                    head_timeTitle(bold_('   >>>  QUENTE  <<<', 1), True, 0.03)
                elif chute<numMach:
                    head_timeTitle(bold_('    >>>  FRIO  <<<', 6), True, 0.03)
            else:
                if chute>1000:
                    head_timeTitle(undl_('Jogada desperdiçada', 3), True, 0.04)
                elif chute==0:
                    head_timeTitle(bold_('Você desistiu?', 1), False, 0.07)
                    loading_tx(False,'.', 3, 1, 1, 0.35)
                    head_timeTitle(bold_('...Fraco!..', 1), True, 0.1)
                    head_timeTitle(neutro_('Vai querer uma...', 1), False, 0.04)
                    head_timeTitle(neutro_('revanche', 2), False, 0.15)
                    head_timeTitle(neutro_(' ?...', 1), True, 0.4)
                    break
        elif chute==numMach:
            head_timeTitle(bold_('...droga', 2), False, 0.07)
            loading_tx(False,'.', 3, 2, 1, 0.35)
            head_timeTitle(bold_('...você achou..', 2), True, 0.12)
            head_timeTitle(neutro_('Aceita', 2), False, 0.06)
            loading_tx(False,'.', 3, 2, 1, 0.35)
            head_timeTitle(neutro_(f'...minha {undl_('revanche', 1)}{neutro_(' ?..', 2)}', 2), True, 0.12)
            break
        t+=1
        head_timeTitle(bold_(f' {t}º chute:', 8), False)
        chute = readn_cleanNum(f' {cor_nat(4)}')
        print(cor_nat(), end=' ')
        loading_tx(False,'>', 3, 3, 1, 0.35)
        #loading_(False,3,4,1,0.1)

    print(' '*1, end='')
    arrasta_pLadoTxt(f'[ {bold_('Revanche', 8)} ]', True, 7, 4, 4, 1, 0.02)
    head_timeTitle(f' {bold_('-'*24, 4)}', True, 0.02)    
    head_timeTitle(f'   [{bold_('1', 4)}] {bold_('Revanche', 7)}')
    head_timeTitle(f'   [{bold_('2', 4)}] {bold_('Parar', 7)}')
    head_timeTitle(f'{bold_('   Seu desejo', 8)} ', False)
    desejo = readn_cleanNum(f'[{cor_bold(4)}')
    print(cor_bold(), end='')
    while desejo not in (1, 2):
        head_timeTitle(f'   Apenas 1 ou 2 ', True)
        head_timeTitle(f'{bold_('   Seu desejo', 8)} ', False)
        desejo = readn_cleanNum(f'[{cor_bold(4)}')
        print(cor_bold(), end='')
    if desejo==1:
        head_timeTitle(neutro_('   Muito bem...hehehe!', 1))
        loading_tx(False,'.', 3, 3, 1, 0.35)
    elif desejo==2:
        head_timeTitle(neutro_('   Até a próxima', 8), False, 0.14)
        loading_tx(False,'.', 3, 3, 2, 0.45)
        head_timeTitle('...')
        break

head_timeTitle(f' {bold_('-'*26, 4)}', True, 0.02)   
print(' '*1, end='')
arrasta_pLadoTxt(f'[ {bold_('Finalizado', 8)} ]', True, 7, 4, 4, 1, 0.02)


