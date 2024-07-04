from random import randint
from time import sleep
nPessoas = int(input('Nº de pessoas no grupo: '))
grupo = []
rg = []
i = []
#nome
#sexo
#idade
for g in range(0, nPessoas):
    grupo.append({})
    rga = randint(100,nPessoas+110)
    grupo[g]["RG"] = rga
    rg.append(rga)
    print('-'*11)
    grupo[g]["Nome"] = str(input('Nome: ')).title()
    grupo[g]["Idade"] = int(input('Idade: '))
    i.append(grupo[g]["Idade"])
    grupo[g]["Sexo"] = str(input('Sexo: ')).lower()
    while grupo[g]["Sexo"] not in 'm, masculino, homem, masc, f, feminino, mulher, fem':
        grupo[g]["Sexo"] = str(input('[ERRO] Escreva certo seu sexo: ')).lower()

sleep(1.5)
#total pessoas
print('=-'*11)
if len(grupo)==1:
    print('Foi cadastrada uma única pessoa!')
else:
    print(f'Foram cadastradas {len(grupo)} pessoas!')

sleep(1)
#média idade
print('-'*11)
print(f'O grupo tem uma média de {sum(i)/len(grupo):.2f} anos.')

sleep(1)
#todas mulheres
print('-'*11)
m = []
for mm in grupo:
    if mm["Sexo"] in ['f', 'feminino', 'fem', 'mulher']:
        m.append(mm)
if len(m)==0:
    print('Sem mulheres no grupo!')
elif len(m)==1:
    print(f'{m[0]["Nome"]} é a única mulher do grupo.')
elif len(m)>=2:
    for a in m:
        if a==m[0]:
            print(f'De mulheres temos: {a["Nome"]}, ', end='')
        elif a==m[-1]:
            print(f'e {a["Nome"]}.')
        else:
            print(f'{a["Nome"]}, ', end='')

sleep(1)
#pessoas idade acima média
print('-'*11)
iAcima = []
for iAc in grupo:
    if iAc["Idade"]>sum(i)/len(grupo):
        iAcima.append(iAc)
if len(iAcima)==0:
    print('Ninguém acima da média de idade do grupo.')
elif len(iAcima)==1:
    print(f'{iAcima[0]["Nome"]}, com {iAcima[0]["Idade"]} anos, é a única pessoa com idade acima da média do grupo.')
elif len(iAcima)>=2:
    for iAcm in iAcima:
        if iAcm==iAcima[0]:
            print(f'Pessoas com idade acima da média temos:\n{iAcm["Nome"]}, com {iAcm["Idade"]};')
        elif iAcm==iAcima[-1]:
            print(f'E {iAcm["Nome"]}, com {iAcm["Idade"]}.')
        else:
            print(f'{iAcm["Nome"]}, com {iAcm["Idade"]};')
print('=-'*11)

    