from datetime import date
print('Lembre-se, obrigatório se alistar aos seus 18 anos!!')
year = int(input('Ano de nascimento: '))
yearAtual = date.today().year
age = int(yearAtual-year)
resta = 18-age

if age>=0 and age<18:
    print(f'Você tem apenas {age} ano(s), ainda falta(m) {resta} anos para alcançar a maioridade.')
    print(f'Obrigatório se apresentar ao exército até o final de {yearAtual+resta}!')
elif age==18:
    print(f'Você já tem {age} anos, seu alistamento é obrigatório!')
    print(f'Portanto, se apresente até o final de {yearAtual+resta}!')
elif age>18:
    ausente = yearAtual-(age-18)
    print(f'Você tinha até {ausente} para se alistar!')
    print(f'Você passou do tempo de alistamento!')
    print(f'Uma multa será gerada no seu nome!')
elif age<0:
    print(f'[ERRO] "{year}" data inválida! Digite ano de nascimento válido.')



