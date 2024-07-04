print('Seja bem vindo ao AlugaCar!!')
print('R$60 a diária e R$0,15 por Km.')

alugaDia = 60
alugaKm = 0.15
dias = float(input('Quantos dias alugado? '))
kms = float(input('Quantos Km rodado? '))
result = (dias*alugaDia)+(kms*alugaKm)

print(f'Você alugou o carro por {dias:.0f} dias e rodou {kms}Km.')
print(f'Portanto, o total a pagar é de R${result:.2f}!')


