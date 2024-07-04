#v2 com referências da aula
from random import choice, randint
sorTupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Valores sorteados: ', end='')
for sort in range(0, 5):
    print(f'{sorTupla[sort]} ', end='')
print('')
print(f'Maior valor sorteado: {max(sorTupla)}')
print(f'Menor valor sorteado: {min(sorTupla)}')    
