print('Seja bem vindo(a) ao Viage Fácil!!')
print('Temos dois preços de viagens:')
print('Até 200km cobramos R$0,50 por Km viajado;')
print('Viagens mais longas apenas R$0,45 por Km viajado.')

destino = float(input('Quantidade de Km até seu destino: '))

if destino<=200:
    priceLow = destino*0.50
    print(f'Sua viagem custará R${priceLow:.2f}!')
else:
    priceHigh = destino*0.45
    print(f'Sua viagem custará R${priceHigh:.2f}!')



''' - v2-simplificada

price = destino*0.50 if destino<=200 else destino*0.45
print(f'Sua viagem custará R$(price:.2f)!') 

'''

