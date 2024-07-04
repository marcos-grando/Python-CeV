from random import randint

print('--'*17)
print(f"{'MEGA SENA':^34}")
print('--'*17)

jogos = int(input('Números de palpites desejados: '))
print('--'*17)

lista = []
for ms in range(0,jogos):
    lista.append([])
    for mms in range(0,6):
        lista[ms].append(randint(1,60))
    print(f'{ms+1}º jogo: {lista[ms]}')
print('')
print(f'{" < Boa Sorte > ":-^34}')
