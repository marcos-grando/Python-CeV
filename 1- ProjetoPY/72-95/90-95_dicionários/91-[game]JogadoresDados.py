from random import randint
from time import sleep
import sys

print('='*51)
print(f'{'Cada jogador lançará 3 dados uma única vez!':^51}')
print(f'{'Somado os valores...o maior vence!':^51}')
print('='*51)

jDict = []
win = []
c=0
while True: #
    print('-'*51)
    jogador = str(input('Player: '))
    if jogador.lower()=='stop':
        break
    jDict.append({})
    jDict[c]["Jogador"] = jogador
    jDict[c]["Dados"] = [randint(1,6), randint(1,6), randint(1,6)]
    while sum(jDict[c]["Dados"]) in win:
        jDict[c]["Dados"] = [randint(1,6), randint(1,6), randint(1,6)]
    jDict[c]["Jogada"] = sum(jDict[c]["Dados"])
    win.append(jDict[c]["Jogada"])
    
    print(f'{jDict[c]["Jogador"]} lançou os 3 dados...')
    sleep(1.5)
    print('*Dados parando de girar*... ', end='')
    for dados in jDict[c]["Dados"]:
        sys.stdout.flush()
        sleep(1)
        print(f'[{dados}]', end='')
    print('')
    sleep(1)
    print(f'{jDict[c]["Jogador"]} lançou: [{jDict[c]["Dados"][0]}] [{jDict[c]["Dados"][1]}] [{jDict[c]["Dados"][2]}]')   
    c+=1

ord = sorted(jDict, key=lambda dicionario: dicionario["Jogada"], reverse=True)
print('')
print('-=-'*17)
print(f'{f'O CAMPEÃO É...{ord[0]["Jogador"]} ! Jogada de: {ord[0]["Jogada"]} pontos.':^51}')
print('-=-'*17)
print('')
print('Tabela:')
print('-'*11)
f=11
print(f'{'Colocação':<{f}} | {'Player':^{f}} | {'Pontuação (Pont. 3 dados)':>16}')
c=0
for w in ord:
    print(f'{f'{c+1}ºlugar':<{f}} | ', end='')  
    print(f'{f'{w["Jogador"]}':^{f}} | ', end='') 
    print(f'{f'{w["Jogada"]} pontos -> [{w["Dados"][0]}] [{w["Dados"][1]}] [{w["Dados"][2]}]':>16}')
    c+=1
