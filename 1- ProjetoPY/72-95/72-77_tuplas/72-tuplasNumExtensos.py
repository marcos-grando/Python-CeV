ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
print('-'*30)
print('Digite "21" p/ parar!')
print('-'*30)
while True:
    dig = int(input('Digite um número [0 à 20]: '))
    while dig not in range(0, 21+1):
        print(f"[ERRO] Número '{dig}' inválido!")
        print('')
        dig = int(input('Digite um número [0 à 20]: '))
    if dig==21:
        break
    print(f'Você digitou o número {ext[dig]}')
    print('-'*32)
print('ixtop')