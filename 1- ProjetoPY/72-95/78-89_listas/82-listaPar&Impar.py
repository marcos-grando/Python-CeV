lista = []
lisPar = []
lisImpar = []
c=0
while True:
    num = int(input(f'{c+1}º número: '))
    if num==999:
        print(f'Lista: {lista}; T= {len(lista)}')
        print(f'Par: {lisPar}; T= {len(lisPar)}')
        print(f'Ímpar: {lisImpar}; T= {len(lisImpar)}')
        break
    lista.append(num)
    if num%2==0:
        lisPar.append(num)
    if num%2!=0:
        lisImpar.append(num)
    