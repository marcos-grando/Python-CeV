print('-=-'*27)
print('Nosso financiamento aceita apenas prestação mensal no valor de até 30% de seu salário!')
print('-=-'*27)

salario = float(input('Nos diga seu salário: R$'))
casaValor = float(input('Valor do imóvel desejado: R$'))
quitarAnos = int(input('Quitação de dívida em quantos anos? '))
quitarMeses = quitarAnos*12
prest = float(casaValor/quitarMeses)

if prest<=(salario*0.30):
    print(f'Você pagará {quitarMeses}x (por {quitarMeses/12:.0f} anos) de R${prest:.2f}!')
elif prest>(salario*0.30):
    print(f'[NEGADO] A prestação de R${prest:.2f} excede 30% de seu salário (R${salario*0.30})')





