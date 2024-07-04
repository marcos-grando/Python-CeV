total=cont1=menor=0

while True:
    print('---- Registre o produto da compra ----')
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total+=preço
    if preço>1000:
        cont1+=1
    if preço<menor or cont1==1:
        menor=preço
        barato=produto
    go = str(input('Continuar?[s/n] ')).lower()
    while go not in ('s','n','sim','não','ss','nn'):
        go = str(input('Continuar?[s/n] ')).lower()
    if go in ('n','nn','não','nao'):
        break
print(f'Total gasto: R${total}')
print(f'Acima de R$1mil: {cont1} compras')
print(f'Produto mais barato: {barato}')
