# releitura exec'28-.py'
from random import choice

num = int(input('[Máx 20] Diga até qual número devo escolher: '))
lista = []
while num>20:
    num = int(input('[ERRO] Digite um número válido (máx 20): ')) 
for n in range(0, num+1):
    lista.append(n)

print(lista)
pcNum = choice(lista)
print('\033[35m-=-\033[m'*17)
print(f'Vou pensar em 1 número de 0 à {num}. Tente adivinhar...')
print('\033[35m-=-\033[m'*17)
player = int(input('Adivinhou? Diga, qual número eu escolhi: '))
print(pcNum)
t = 0

while True:
    if pcNum==player:
        print('\033[32m-=-\033[m'*10)
        print(f'!!![BINGO] Você acertou!!!')
        print(f'TTotal de tentativas: {t+1}x.')
        print('\033[32m-=-\033[m'*10)
        break
    while player>num:
        player = int(input(f'[ERRO] Escolha um número até {num}: '))
        if pcNum==player:
            print('\033[32m-=-\033[m'*10)
            print(f'!!![BINGO] Você acertou!!!')
            print(f'Total de tentativas: {t+1}x.')
            print('\033[32m-=-\033[m'*10)
            break
    player = int(input('[LOSE] Você errou, tente novamente: '))
    t+=1
