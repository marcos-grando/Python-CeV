def lerint(mensagem):
    número_inteiro = input(mensagem)
    while número_inteiro.isnumeric()==False:
        print('[ERRO] Apenas números inteiros!')
        número_inteiro = input(mensagem)
    if número_inteiro.isnumeric()==True:
        número_inteiro = int(número_inteiro)
    return número_inteiro

x = lerint('Digite um n: ')
print(f'Você digitou o número {x} !')
print(x+2)
