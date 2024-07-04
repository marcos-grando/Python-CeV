from mydefs_package.money_mdl.defs_money import money_metade,money_dobro,money_aumentar,money_diminuir

valor = float(input('Preço: R$'))
print('-'*32)

print(f'A metade de R${valor:.2f} é: R${money_metade(valor):.2f}\n', '-'*32)
print(f'O dobro de R${valor:.2f} é: R${money_dobro(valor):.2f}\n', '-'*32)
print(f'R${valor:.2f} +15%, temos: R${money_aumentar(valor, 10):.2f}\n', '-'*32)
print(f'R${valor:.2f} -15%, temos: R${money_diminuir(valor, 10):.2f}\n', '-'*32)
