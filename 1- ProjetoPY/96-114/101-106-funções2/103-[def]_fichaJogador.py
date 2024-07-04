def ficha(nome_jogador, gols_jogador='0'):
    print('-='*20)
    print(f'O jogador {nome_jogador} fez {gols_jogador} gol(s) !')
    print('-='*20)

while True:
    print('-'*17)
    jogador = str(input('Nome do jogado: '))
    if jogador=='stop':
        break
    elif jogador=='':
        jogador = '<não informado>'
    
    gols = input('Gols do jogador: ')
    if gols=='':
        gols = '0'
    elif gols.isnumeric()==False:
        gols = input('[ERRO] Apenas números: ')
    print('-'*17)
    ficha(jogador, gols)
