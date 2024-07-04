listaCores = {'limpar':'\033[m', 'vermelho':'\033[31m', 'azul':'\033[34m', 'verde':'\033[32m'} 
from time import sleep

print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)

while True:
    opt = int(input('>>>Opções de cáculos:\n   [1] Adição\n   [2] Multiplicação\n   [3] Qual maior?\n   [4] Novos números\n   [5] Sair do programa\n>>>Qual operação deseja: '))
    print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
    while opt not in (1, 2, 3, 4, 5):
        print(f'{listaCores["vermelho"]}-=-{listaCores["limpar"]}'*9)
        print(f"[ERRO] Opção '{opt}' inválida!")
        print(f'{listaCores["vermelho"]}-=-{listaCores["limpar"]}'*9)
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
        opt = int(input('>>>Opções de cáculos:\n   [1] Adição\n   [2] Multiplicação\n   [3] Qual maior?\n   [4] Novos números\n   [5] Sair do programa\n>>>Qual operação deseja: '))
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
    while opt==4:
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
        n1 = int(input('Digite primeiro número: '))
        n2 = int(input('Digite segundo número: '))
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
        opt = int(input('>>>Opções de cáculos:\n   [1] Adição\n   [2] Multiplicação\n   [3] Qual maior?\n   [4] Novos números\n   [5] Sair do programa\n>>>Qual operação deseja: '))
        print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
    if opt in (1, 2, 3):   
        print(f'{listaCores["verde"]}-=-{listaCores["limpar"]}'*9)
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
        print(f'{listaCores["verde"]}-=-{listaCores["limpar"]}'*9)
    elif opt==5:
        break  
    sleep(2)
    print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
    go = input('Deseja continuar?[s/n] ').lower().strip()
    while go not in ('s', 'sim', 'si', 'yes'):
        if go=='n' or go=='não' or go=='no' or go=='nao':
            break
        else:
            print(f"[ERRO] Opção '{go}' inválida!")
        go = input('Deseja continuar?[s/n] ').lower().strip() 
    print(f'{listaCores["azul"]}-=-{listaCores["limpar"]}'*11)
print(f'{listaCores["vermelho"]}-=-{listaCores["limpar"]}'*11)
print(f'{listaCores["vermelho"]}-=--=--=--=--={listaCores["limpar"]} FIM {listaCores["vermelho"]}=--=--=--=--=-{listaCores["limpar"]}')
