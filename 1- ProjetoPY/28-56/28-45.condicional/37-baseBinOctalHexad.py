print('-=-'*20)
print('''Opções de base para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
print('-=-'*20)

option = int(input('Digite a conversão escolhida: '))

if option == 1:
    num = int(input('Número inteiro para conversão: '))
    print(f'O número {num} convertido para Binário é {bin(num)[2:]}!!')
elif option == 2:
    num = int(input('Número inteiro para conversão: '))
    print(f'O número {num} convertido para Octal é {oct(num)[2:]}')
elif option == 3:
    num = int(input('Número inteiro para conversão: '))
    print(f'O número {num} convertido para Hexadecimal é {hex(num)[2:]}')
elif option!=1 and option!=2 and option!=3:
    print(f'\033[1;31;40m[ERRO]\033[m O {option} não é uma opção válida!')