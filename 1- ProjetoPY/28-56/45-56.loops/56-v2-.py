somaIdade = 0
mediaIdade = 0
maioridadeHomem = 0
nomeVelho = ''
mulherNova = 0
for p in range(1, 3+1):
    print(f'-----{p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaIdade += idade
    if p==1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade>maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade<20:
        mulherNova += 1
mediaIdade = somaIdade/3
print(mediaIdade)
print(maioridadeHomem, nomeVelho)
print(mulherNova)