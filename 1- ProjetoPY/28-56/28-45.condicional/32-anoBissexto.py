year = int(input('Qual ano você quer analisar? '))
if year%4==0 and year%100!=0 or year%400==0:
    print(f'O ano {year} É bissexto!')
else:
    print(f'O ano {year} NÃO É bissexto!')
