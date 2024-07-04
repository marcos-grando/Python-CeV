produtoValor = float(input('Preço do produto: R$'))
produtoDesconto = float(input('Porcentagem de desconto: '))
desconto = float((produtoDesconto/100)*produtoValor)
novoValor = produtoValor-desconto

print(f'Seu produto de R${produtoValor} recebeu um desconto de {produtoDesconto}% !')
print(f'Você pagará R${novoValor}, desconto de R${desconto}.')


