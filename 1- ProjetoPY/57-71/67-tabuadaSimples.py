while True:
    tabuada = int(input('Quer tabuada de qual valor? '))
    print('-=-'*10)
    if tabuada<0:
        break
    else:
        for tab in range(1, 10+1, 1):
            print(f'{tabuada} x {tab} = {tabuada*tab}')
        print('-=-'*10)
print('Programa encerrado! Volte sempre.')

#exerc sem enrolação, seguindo 100% oq foi pedido