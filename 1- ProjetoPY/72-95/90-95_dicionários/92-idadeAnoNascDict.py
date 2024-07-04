from datetime import date
yAtual = date.today().year

infos = []
ps = 3

print('-='*22)
for c in range(0,ps):
    print('--'*11)
    nome = str(input('Nome: ')).strip().title()
    if nome.lower()=='stop':
        break
    infos.append({})
    infos[c]["Nome"] = nome
    infos[c]["Data"] = int(input('Ano de nascimento: '))
    infos[c]["Idade"] = yAtual-infos[c]["Data"]
    infos[c]["Ctps"] = int(input('Digite sua CTPS: '))
    if infos[c]["Ctps"]!=0:
        infos[c]["ContratoAno"] = int(input('Ano contratado: '))
        infos[c]["Salário"] = float(input('Salário: '))
    infos[c]["Aposenta"] = 35-(yAtual-infos[c]["ContratoAno"])
print('--'*11)
print('-='*22)
print('--'*11)
for p in infos:
    if ["Ctps"]==0:
        print(f'{p["Nome"]}, {p["Idade"]} anos, possui CTPS inválida para cadastro!')
    else:
        print(f'{p["Nome"]}, {p["Idade"]} anos, se aposentará em {yAtual+p["Aposenta"]}, daqui {p["Aposenta"]} anos.')
    print('--'*11)
print('-='*22)

print(infos)
