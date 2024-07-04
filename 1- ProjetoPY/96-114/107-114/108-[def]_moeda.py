from mydefs_package.money_mdl.defs_money import money_metade,money_dobro,money_aumentar,money_diminuir,money_moeda

valor = float(input('Preço: R$'))
print('-'*32)

print(f'A metade de {money_moeda(valor)} é: {money_moeda(money_metade(valor))}\n', '-'*32)
print(f'O dobro de {money_moeda(valor)} é: {money_moeda(money_dobro(valor))}\n', '-'*32)
print(f'{money_moeda(valor)} +15%, temos: {money_moeda(money_aumentar(valor, 10))}\n', '-'*32)
print(f'{money_moeda(valor)} -15%, temos: {money_moeda(money_diminuir(valor, 10))}\n', '-'*32)

#exerc108 é o ex107 apenas com função de formatação 'money_moeda()'