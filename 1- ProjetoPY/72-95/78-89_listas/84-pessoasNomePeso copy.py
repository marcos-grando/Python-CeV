#Teste descontinuado (podendo excluir)

listas = [[],[],[]]

print(f'Cadastre seu grupo abaixo: ["stop" para finalizar]')
while True:
    nome = str(input('Nome: ')).strip().title()
    if nome.lower()=='stop':
        break
    peso = float(input('Peso: '))
    idade = int(input('Idade: '))
    listas[0].append(nome)
    listas[1].append(peso)
    listas[2].append(idade)

print(listas)
print(sorted(listas))

'''
if len(listas)==0:
    print('Programa encerrado! Nenhuma pessoa cadastrada.')
else:

    print(f'Total de {len(listas)} cadastros efetivados !')
    print(f'Mais pesado: {sorted(listas)[-1][1]}, com {sorted(listas)[-1][0]}kg !')
    print(f'Mais leve: {sorted(listas)[0][1]}, com {sorted(listas)[0][0]}kg !')

    go = int(input('Ver todos cadastrados?\n[1] Sim\n[2] Não\nOpção: '))
    if go==1:
        print(f'Os {len(listas)} cadastrados são: ')
        for c in range(0, len(listas)):
            if listas[c]!=listas[-1]:
                print(f'{listas[c][1]}, com {listas[c][0]}kg;')
            elif listas[c]==listas[-1]:
                print(f'E {listas[c][1]}, com {listas[c][0]}kg.')
        print(f'Programa encerrado!')
    elif go==2:
        print(F'Programa encerrado!')

'''