primo = int(input('Número para investigar se é primo: '))
print('-=-'*12)
lista = []
lixeira = []
for a in range(1, primo+1, +1):
    if primo%a==0:
        lista.append(a)
    else:
        lixeira.append(a)
if len(lista)==2:
    print(f'Número {primo} É um número primo!')
    print('')
    print(f'Número divisível apenas por {lista}.')
elif len(lista)>2:
    print(f'Número {primo} NÃO É um número primo!')
    print('')
    print(f'Número divisível por {lista}')
print('-=-'*12)
