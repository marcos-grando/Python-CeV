from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.defsGood_mdl.defsGood import loading_
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from random import randint
from time import sleep

loading_()
head_timeTitle(f'{f'{bold_('='*56, 4)}'}')
head_timeTitle(f'{f'{bold_('The Machine ', 1)}{neutro_('escolherá ', 8)}{undl_('3 números', 8)}{neutro_(' entre 1~10')}':^{92}}')
head_timeTitle(f'{f'{neutro_('Você terá ', 8)}{bold_('4 chances ', 2)}{neutro_('de adivinhar cada número')}':^{82}}')
head_timeTitle(f'{f'{bold_('-'*56, 4)}'}')

head_timeTitle(f'{f'Seu chute foi {undl_('acima', 1)} do número misterioso?{bold_('   >>>  QUENTE  <<<', 1)}':>{52}}')
head_timeTitle(f'{f'Seu chute foi {undl_('abaixo', 6)} do número misterioso?{bold_('   >>>  FRIO  <<<', 6)}':>{52}}')
head_timeTitle(f'{f'{bold_('-'*56, 4)}'}')

machineNuns = []
while len(machineNuns)!=3:
    machineEscolha = randint(1,10)
    while machineEscolha in machineNuns:
        machineEscolha = randint(1,10)
    else:
        machineNuns.append(machineEscolha)

loading_()

for round in range(3):
    if round==0:
        head_timeTitle(f'{f'{undl_('PRIMEIRO NÚMERO!', 4)}'}')
    elif round==1:
        head_timeTitle(f'{f'{undl_('SEGUNDO NÚMERO!', 4)}'}')
    elif round==2:
        head_timeTitle(f'{f'{undl_('TERCEIRO NÚMERO!', 4)}'}')
    chutes = 0
    for tentat in range(4):
        if tentat<4:
            head_timeTitle(neutro_(f'{tentat+1}ª tentativa:'), False)
        else:
            head_timeTitle(neutro_(f'Última tentativa:'), False)
        chute = readn_cleanNum(' ')
        chutes+=1
        loading_(1,3,3,1)
        if chute>machineNuns[round] and chute<=10 and chutes<4:
            print(bold_('   >>>  QUENTE  <<<', 1))
        elif chute<machineNuns[round] and chute<=10 and chutes<4:
            print(bold_('    >>>  FRIO  <<<', 6))
        elif chute>10 or chute==0:
            print(undl_('Jogada desperdiçada.', 3))
        elif chutes==4 and chute!=machineNuns[round]:
            fim=True
            break
        else:
            print(bold_('     ** ACHOU! **', 3))
            fim=False
            break
    if fim==True:
        loading_(1,3,5,1)
        break
print('-'*22)   
if fim==True:
    print(bold_('  +++  GAMEOVER  +++', 1))
else:
    print(bold_('  !!!  PARABÉNS  !!!', 2))
    print(neutro_('Você adivinhou os 3 números.', 2))
