cont0=cont1=cont2= 0
print('-'*25)
while True:
    
    print('   CADASTRE UMA PESSOA')
    print('-'*25)

    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in ('m', 'f'):
        sexo = str(input('Sexo:[m/f] ')).strip().lower()
    if idade>=18:
        cont0+=1
    if sexo=='m':
        cont1+=1
    if idade<18 and sexo=='f':
        cont2+=1
    print('-'*25)

    go = str(input('Continuar?[s/n] ')).strip().lower()
    while go not in ('s', 'n'):
        go = str(input('Continuar?[s/n] ')).strip().lower()
    if go=='n': break   
    print('-'*25)

print('-'*25)
print(f'Maiores de 18 anos: {cont0} pessoas.')
print(f'Total de homens: {cont1} presentes.')
print(f'Mulheres menores de 18: {cont2} ao todo.')
print('')
