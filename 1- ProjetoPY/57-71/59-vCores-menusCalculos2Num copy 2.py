from mydefs_package.mycores_mdl.mycores import *
from time import sleep

print(neutro_('-=-'*11, 4))
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
print(neutro_('-=-'*11, 4))

while True:
    opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: '''))
    print(neutro_('-=-'*11, 4))
    while opt not in (1, 2, 3, 4, 5):
        print(neutro_('-=-'*9, 1))
        print(f"[ERRO] Opção '{opt}' inválida!")
        print(neutro_('-=-'*9, 1))
        print(neutro_('-=-'*11, 4))
        opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: '''))
        print(neutro_('-=-'*11, 4))
    while opt==4:
        print(neutro_('-=-'*11, 4))
        n1 = int(input('Digite primeiro número: '))
        n2 = int(input('Digite segundo número: '))
        print(neutro_('-=-'*11, 4))
        print(neutro_('-=-'*11, 4))
        opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: '''))
        print(neutro_('-=-'*11, 4))
    if opt in (1, 2, 3):   
        print(neutro_('-=-'*9, 2)) 
        if opt==1:
            print(f'Adição: {n1} + {n2} = {n1+n2}')
        elif opt==2:
            print(f'Multiplicação: {n1} x {n2} = {n1*n2}')
        elif opt==3:
            if n1==n2:
                print(f'Números iguais!')
            else:
                lis = [n1, n2]
                ord = sorted(lis)
                print(f'Maior>Menor: {ord[1]} > {ord[0]}!')
        print(neutro_('-=-'*9, 2))
    elif opt==5:
        break  
    sleep(2)
    print(neutro_('-=-'*11, 4))
    go = input('Deseja continuar?[s/n] ').lower().strip()
    while go not in ('s', 'sim', 'si', 'yes'):
        if go=='n' or go=='não' or go=='no' or go=='nao':
            break
        else:
            print(f"[ERRO] Opção '{go}' inválida!")
        go = input('Deseja continuar?[s/n] ').lower().strip() 
    print(neutro_('-=-'*11, 4))
print(neutro_('-=-'*9, 1))
print(f'{neutro_('-=-'*5, 1)} FIM {neutro_('-=-'*5, 1)}')
