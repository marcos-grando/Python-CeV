from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.defsGood_mdl.defsGood import loading_,loading_tx
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from locale import LC_MONETARY, currency, setlocale
setlocale(LC_MONETARY, 'pt_BR.UTF-8')
from random import randint
from time import sleep
def traço_vertical(mensagem, speed=0.05, espaço_esq=0, espaço_dir=0):
    print(bold_('|'+' '*espaço_esq, 8), end='')
    head_timeTitle(mensagem, False, speed)
    print(bold_(' '*espaço_dir+'|', 8))
bilheteUsado = 1
sorteio = [1,5,7,6,4,8] 
meusBilhetes = [[12,16,6,17,18,4],[16,5,18,51,1,49]]
meusAcertos = []
recompensasReal = ['100', '1000', '10000']

