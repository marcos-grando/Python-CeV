#versão Guanabara
from math import floor
from time import sleep
print('='*30)
print(' '*10, 'BANCO MAG')
print('='*30)
print('Insira seu cartão!')
sleep(2)
saque = int(input('Valor desejado à sacar: R$'))
print('='*30)
while saque!=0:
    n50=n20=n10=n1=0
    if saque>500:
        n100 = floor(saque/100)
        r100 = n100*100
        saque -= r100
        print(f'Total de {n100} cédulas de R$100,00 ')
        sleep(0.7)
    elif saque>=50:
        n50 = floor(saque/50)
        r50 = n50*50
        saque -= r50
        print(f'Total de {n50} cédulas de R$50,00 ')
        sleep(0.7)
    elif saque>=20:
        n20 = floor(saque/20)
        r20 = n20*20
        saque -= r20
        print(f'Total de {n20} cédulas de R$20,00 ')
        sleep(0.7)
    elif saque>=10:
        n10 = floor(saque/10)
        r10 = n10*10
        saque -= r10
        print(f'Total de {n10} cédulas de R$10,00 ')
        sleep(0.7)
    elif saque>=1:
        n1 = floor(saque/1)
        r1 = n1*1
        saque -= r1
        print(f'Total de {n1} cédulas de R$1,00 ')
print('='*30)







