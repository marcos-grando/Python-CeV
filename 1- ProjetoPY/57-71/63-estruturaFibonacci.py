print('-'*22)
print('Sequência de Fibonacci')
print('-'*22)
print('')
termos = int(input('Quantidade de termos desejada: '))
t1 = 0
t2 = 1
cont = 3
print('-'*22)
print(f'{t1}-> {t2}', end='')
while cont<=termos:
    t3 =  t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> Fim! ')







