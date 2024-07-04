from time import sleep

'''jogadores = [{"Jogador": 'A', "Gols": [1, 4, 2], "Partidas": 3, "GTotal": 4, "Aproveitamento": 148.19648686381 },{"Jogador": 'B', "Gols": [1, 1, 1], "Partidas": 3, "GTotal": 3, "Aproveitamento": 124.26468468546 },{"Jogador": 'C', "Gols": [3, 2, 10], "Partidas": 3, "GTotal": 15, "Aproveitamento": 125},{"Jogador": 'D', "Gols": [0], "Partidas": 0, "GTotal": 0, "Aproveitamento": 100}]'''
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
    if jogadores[c]["Partidas"]!=0:
        jogadores[c]["Aproveitamento"] = float((jogadores[c]["GTotal"]/jogadores[c]["Partidas"])*100)
    c+=1
print('='*30)
print('')
f=15
print(f'{'Jogador':<{f}} | {'Partidas (Gols)':^20} | {'Aproveitamento':>16}')

for j in jogadores:
    if j["Partidas"]>0:
        print(f'{f'{j["Jogador"]}':<{f}} | {f'{j["Partidas"]} jogos ({j["GTotal"]} gols)':^20} | {f'{round(j["Aproveitamento"], 2)}':>14} %') 

for jj in jogadores:
    if jj["Partidas"]==0:
        print(f'Jogador {j["Jogador"]} ainda não teve partida oficial.')
'''
for j in jogadores:
    c=1
    print('-'*15)
    if j["Partidas"]==0:
        print(f'Jogador {j["Jogador"]} ainda não teve partida oficial.')    {(j["GTotal"]/j["Partidas"])*100}
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
print('-'*15)'''