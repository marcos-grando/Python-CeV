from mydefs_package.defsGood_mdl.defsGood import *
from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from random import randint
from locale import LC_MONETARY, currency, setlocale
setlocale(LC_MONETARY, 'pt_BR.UTF-8')
def traço_vertical(mensagem, speed=0.05, espaço_esq=0, espaço_dir=0):
    print(bold_('|'+' '*espaço_esq, 8), end='')
    head_timeTitle(mensagem, False, speed)
    print(bold_(' '*espaço_dir+'|', 8))

a = ['a', 'b']
b = [1, 4]
for n,nn in a(b):
    print(n, nn)





