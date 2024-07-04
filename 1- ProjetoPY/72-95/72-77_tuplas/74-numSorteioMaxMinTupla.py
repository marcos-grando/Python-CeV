from random import choice
tupla = (1,2,3,4,5,6,7,8,9,10)

print(f'Valores sorteados: ', end='')
for sort in range(0, 5):
    sorteado = choice(tupla)
    print(f'{sorteado} ', end='')
    if sort==0:
        maior=menor=sorteado
    if sorteado>maior:
        maior=sorteado
    if sorteado<menor:
        menor=sorteado
print('')
print(f'Maior valor sorteado: {maior}')
print(f'Menor valor sorteado: {menor}')    


