listaCores = {'limpar':'\033[m', 'vermelho':'\033[31m', 'azul':'\033[34m', 'verde':'\033[32m'} 
from time import sleep

print(f'\033[34m-=-\033[m'*11)
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
print(f'\033[34m-=-\033[m'*11)

while True:
    opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: '''))
    print(f'\033[34m-=-\033[m'*11)
    while opt not in (1, 2, 3, 4, 5):
        print(f'\033[31m-=-\033[m'*9)
        print(f"[ERRO] Opção '{opt}' inválida!")
        print(f'\033[31m-=-\033[m'*9)
        print(f'\033[34m-=-\033[m'*11)
        opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: '''))
        print(f'\033[34m-=-\033[m'*11)
    while opt==4:
        print(f'\033[34m-=-\033[m'*11)
        n1 = int(input('Digite primeiro número: '))
        n2 = int(input('Digite segundo número: '))
        print(f'\033[34m-=-\033[m'*11)
        print(f'\033[34m-=-\033[m'*11)
        opt = int(input(
'''>>>Opções de cáculos:
[1] Adição
[2] Multiplicação
[3] Qual maior?   
[4] Novos números   
[5] Sair do programa
>>>Qual operação deseja: ''')) 
        print(f'\033[34m-=-\033[m'*11)
    if opt in (1, 2, 3):   
        print(f'\033[32m-=-\033[m'*9)
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
        print(f'\033[32m-=-\033[m'*9)
    elif opt==5:
        break  
    sleep(2)
    print(f'\033[34m-=-\033[m'*11)
    go = input('Deseja continuar?[s/n] ').lower().strip()
    while go not in ('s', 'sim', 'si', 'yes'):
        if go=='n' or go=='não' or go=='no' or go=='nao':
            break
        else:
            print(f"[ERRO] Opção '{go}' inválida!")
        go = input('Deseja continuar?[s/n] ').lower().strip() 
    print(f'\033[34m-=-\033[m'*11)
print(f'\033[31m-=-\033[m'*11)
print(f'\033[31m-=--=--=--=--=\033[m FIM \033[31m=--=--=--=--=-\033[m')
