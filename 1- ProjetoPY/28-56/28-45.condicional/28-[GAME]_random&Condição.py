from random import choice
print('Seja bem vindo ao game VS COMPUTER!')
nickname = str(input('Digite seu nickname: ')).strip()

print('Nosso COMPUTER irá escolher um número entre 1 e 5!')
print(f'E você, caro(a) {nickname}, precisará adivinhar esse número.')

listaNum = [1, 2, 3, 4, 5]
computerNum = choice(listaNum)
ready = str(input('Pronto? Sim ou Não? '))

if ready.upper()=='SIM'or'SÍM':
    escolhaNum = int(input('Escolhe um número entre 1 e 5: '))
    if escolhaNum==computerNum:
        print(f'PARABÉNS! Nosso COMPUTER também escolheu {computerNum}!')
    if escolhaNum!=computerNum:
        print(f'GAME OVER! Nosso COMPUTER escolheu {computerNum}...')
else:
    print(f'GAME OVER! Você hesitou, você perdeu!')
    
