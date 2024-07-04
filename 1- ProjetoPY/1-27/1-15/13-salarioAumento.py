nome = input('Nome do funcionário: ')
salario = float(input('Salário do funcionário: R$'))
salarioAumento = float(input('Percentual de aumento: '))
salarioNovo = salario+((salarioAumento/100)*salario)

print(f'O funcionário {nome} recebe atualmente R${salario} por mês.')
print(f'Com aumento de {salarioAumento}% ele receberá R${salarioNovo} por mês.')


