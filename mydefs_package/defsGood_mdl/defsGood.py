from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.mycores_mdl.mycores import *
from time import sleep

def loading_tx(fim=False, caract='.', pontos=2, cores=6, repetir=1, tempo=0.02):
    caracLen = len(caract)
    repetições = 0
    while repetições!=repetir:
        for n in range(cores):        # define as cores vão ter //max->7
            for nn in range(pontos):  # define quantas bolotinhas vão ter
                print(f'{bold_(caract, n)}',  end='', flush=True)
                sleep(tempo)
            print('\b'*(pontos*caracLen), end='', flush=True)
        if fim==True:                    # fim=False próximo print substitui os pontos / fim=True os pontos permanecem na linha
            print('')
        repetições+=1

def loading_(fim=False, pontos=2, cores=6, repetir=1, tempo=0.02):
    repetições = 0
    while repetições!=repetir:
        for n in range(cores):        # define as cores vão ter //max->7
            for nn in range(pontos):  # define quantas bolotinhas vão ter
                print(f'{bold_('>', n)}',  end='', flush=True)
                sleep(tempo)
            print('\b'*pontos, end='', flush=True)
        if fim==True:                    # fim=False próximo print substitui os pontos / fim=True os pontos permanecem na linha
            print('')
        repetições+=1
#loading_(1,3,3,1)     #OBS: se colocar print(loading()) -> retorna 'None'

def arrasta_pLado(arrasto=15, speed=0.05, linha=1, cor=4):
    for linha in range(linha):
        for arrasto in range(arrasto):
            print(f'{bold_('-', cor)}',  end='>>\b\b', flush=True)
            sleep(speed)
        print('>>\b\b', end='  ', flush=True)

def arrasta_pLadoTxt(txt, fim=True, corTx=0, cor=4, laterais=0, linhas=1, speed=0.05):
    if laterais==0:
        laterais = len(txt)
    for linha in range(linhas):
        print(f'{neutro_('<<', corTx)}', end='')
        for arrasto in range(laterais*2):
            if arrasto==laterais:
                head_timeTitle(neutro_(txt, corTx), False)
            print(f'{bold_('-', cor)}',  end=f'{neutro_('>>', corTx)}\b\b', flush=True)
            sleep(speed)
        print(f'{neutro_('>>', corTx)}\b\b', end='', flush=True)
    if fim==True:
        print('')
    elif fim==False:
        print(f'{neutro_('>>', corTx)}', end='')



