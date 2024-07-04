salario = float(input('Salário do funcionário: '))
if salario>1250.00:
    salarioHigh = (salario*(10/100))+salario
    print(f'Com o aumento de 10% o novo salário será de R${salarioHigh}!')
if salario<=1250.00:
    salarioLow = (salario*(15/100))+salario
    print(f'Com aumento de 15% o novo salário será de R${salarioLow}')