print('Bem vindo ao Tabuadinha!')
n1 = int(input('Tabuada de: '))
n2 = int(input('Até quanto: '))

for a in range(0, n2+1, +1):
    print(f'{n1}x{a} = {n1*a}')

