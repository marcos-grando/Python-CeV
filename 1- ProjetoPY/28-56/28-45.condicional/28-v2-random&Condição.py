# versão do Guanabara 
from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensasr em um  número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
escolhaNum = int(input('Em que número eu pensei? '))
computerNum = randint(0,5)

print('PROCESSANDO...')
sleep(3)

if escolhaNum==computerNum:
    print('PARABÉNS! Você conseguiu me vencer...')
if escolhaNum!=computerNum:
    print(f'GAME OVER! Você perdeu, eu escolhi o número {computerNum}!')
 