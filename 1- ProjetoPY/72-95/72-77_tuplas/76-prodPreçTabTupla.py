prodPreç = ('Arroz', 15, 'Feijão', 14, 'Café', 20, 'Açúcar', 8, 'Pão', 5)

for tab in range(0, len(prodPreç), 2):
    print(f'{prodPreç[tab]:.<30}', end='')
    print(f'R$ {prodPreç[tab+1]:>6.2f}')

