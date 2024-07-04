from mydefs_package.money_mdl.defs_money import money_moeda,money_metade,money_dobro,money_aumentar,money_diminuir

valor = float(input('Preço: R$'))
print('-'*32)

x = True

print(f'A metade de {money_moeda(valor)} é: {money_metade(valor, x)}\n', '-'*32)
print(f'O dobro de {money_moeda(valor)} é: {money_dobro(valor, x)}\n', '-'*32)
print(f'{money_moeda(valor)} +15%, temos: {money_aumentar(valor, 15, x)}\n', '-'*32)
print(f'{money_moeda(valor)} -15%, temos: {money_diminuir(valor, 15, x)}\n', '-'*32)

#exerc109 é o ex107/108 apenas com função de [escolha] à função/formatação 'money_moeda()'