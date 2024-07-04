from math import floor
from time import sleep
print('='*30)
print(' '*10, 'BANCO SAQ')
print('='*30)

print('Insira seu cartão!')
sleep(1)

saque = int(input('Valor de saque: R$'))
notas = [200,100,50,20,10,5,1]
cont=0
print('')
while True:
    notasSacadas = floor(saque/notas[cont])
    saque %= notas[cont]
    if notasSacadas>0:
        print(f'Total de {notasSacadas} cédulas de R${notas[cont]}')
        sleep(0.7)
    if notas[cont]==notas[-1]:
        break
    cont+=1
print('')
print('='*30)
