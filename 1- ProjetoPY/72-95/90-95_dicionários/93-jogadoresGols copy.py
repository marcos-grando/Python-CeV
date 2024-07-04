from time import sleep

jogadores = []
c=0

while True:
    print('-'*15)
    jogador = str(input('Nome do jogador: ')).title().strip()
    if jogador.lower()=='stop':
        break
    jogadores.append({})
    jogadores[c]["Jogador"] = jogador
    partidas = int(input('Partidas jogadas: '))
    if partidas==0:
        jogadores[c]["Gols"] = [0]
    elif partidas==1:
        jogadores[c]["Gols"] = [int(input('Gols na partida: '))]
    else:
        jogadores[c]["Gols"] = []
        for p in range(0, partidas):
            sleep(0.5)
            jogadores[c]["Gols"].append(int(input(f'Gols na {p+1}º partida: ')))
    jogadores[c]["Partidas"] = partidas
    jogadores[c]["GTotal"] = sum(jogadores[c]["Gols"])
    c+=1
print('-'*15)
print('')

for j in jogadores:
    c=1
    print('-'*15)
    if j["Partidas"]==0:
        print(f'Jogador {j["Jogador"]} ainda não teve partida oficial.')
    if j["Partidas"]!=0 and j["Gols"]==0:
        print(f'{j["Jogador"]} fez NENHUM gol em {j["Partidas"]} partida(s).')
    if j["Gols"]!=0:
        print(f'Jogador {j["Jogador"]}, com total de {j["GTotal"]} gols em {j["Partidas"]} partidas, fez:')
        for g in j["Gols"]:
            if g==1:
                print(f'{g} gol na {c}º partida')
            elif g>=2:
                print(f'{g} gols na {c}º partida')
            c+=1
print('-'*15)