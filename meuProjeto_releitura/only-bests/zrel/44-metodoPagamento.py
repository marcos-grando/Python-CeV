produtoPreço = float(input('Preço do produto: R$'))
print('''Método de pagamento:
[1] À vista boleto/pix - 10% de desconto!
[2] À vista no cartão - 5% de desconto!
[3] Parcelado em até 2x - Sem juros!
[4] Parcelado em 3x ou mais - 20% de juros!''')
option = int(input('Qual método de pagamento: '))

if option==1:
    print(f'Você pagará R${produtoPreço-(produtoPreço*0.10)} no pix/boleto!')
elif option==2:
    print(f'Você pagará R${produtoPreço-(produtoPreço*0.05)} no cartão!')
elif option==3:
    print(f'1x de R${produtoPreço} no cartão de crédito!')
    print(f'2x de R${produtoPreço/2} no cartão de crédito!')
elif option==4:
    parcelas = int(input('Em quantos vezes você gostaria de parcelar: '))
    parcelaComJuros = (produtoPreço/parcelas)+((produtoPreço/parcelas)*0.20)
    print(f'{parcelas}x de R${parcelaComJuros} no cartão de crédito!')
    print(f'Totalizando R${parcelaComJuros*parcelas} no cartão de crédito!')



    