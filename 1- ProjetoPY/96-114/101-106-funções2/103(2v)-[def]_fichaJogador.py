def ficha(nome_jogador, gols_jogador='>sem info<'):
    if not nome_jogador:
        nome_jogador = '>não informado<'
    if gols_jogador.isnumeric()==False:
        gols_jogador = '>sem info<'
    print('-='*33)    
    print(f'O jogador {nome_jogador} fez um total de {gols_jogador} gol(s) no campeonato!')
    print('-='*33)

while True:
    print('--'*11)
    nomeJogador = str(input('Nome do jogador: '))
    if nomeJogador=='stop':
        break
    golsJogador = input('Gols do jogador: ')
    ficha(nomeJogador, golsJogador)

