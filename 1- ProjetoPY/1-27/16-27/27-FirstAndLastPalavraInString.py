name = str(input('Nome completo: ')).strip().title().split()
print(f'Seja bem vindo {name}')
print(f'Seu último nome é {name[len(name)-1]}')
print(f'Seu primeiro nome é {name[0]}')
