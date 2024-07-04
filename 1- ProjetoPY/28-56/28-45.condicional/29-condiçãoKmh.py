print('Bem vindo ao Speed POLICE!')
print('Maior programa policial de controle de velocidade do mundo!')
policeID = input('Seu nome, sr(a) policial: ')
velocidade = float(input(f'Sr(a) {policeID}, digite a velocidade do meliante: '))

if velocidade>80:
    multa = (velocidade-80)*7
    print(f'MULTADO em R${multa:.2f}')
if velocidade<=80:
    print('TÁ SAFE! Pode ir!')
