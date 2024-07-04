from datetime import date

year = int(input('Ano de nascimento: '))
yearAtual = date.today().year
age = int(yearAtual-year)

if age<=9:
    print('MIRIM!')
elif age>9 and age<=14:
    print('INFANTIL!')
elif age>14 and age<=19:
    print('JUNIOR!')
elif age>19 and age<=24:
    print('SÊNIOR!')
elif age>24:
    print('MASTER!')