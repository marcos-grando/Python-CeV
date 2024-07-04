from time import sleep
from mydefs_package.mycores_mdl.mycores import *

def head_title(mensagem):
    print('='*37)
    print(f'{f'{mensagem}':^37}')
    print('-'*37)
    
def head_timeCaract(caracter, vezes):
    for repet in range(vezes):
        print(caracter, end='', flush=True)
        sleep(0.01)
    print('')

def head_timeTitle(mensagem, end=True, speed=0.05):
    for letra in mensagem:
        print(letra, end='', flush=True)
        sleep(speed)
    if end==True:
        print('')


