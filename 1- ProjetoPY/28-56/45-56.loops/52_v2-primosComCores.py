listaCores = {'azul':'\033[34m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'limpar':'\033[m', 'roxo':'\033[35m'} 
primo = int(input(f'{listaCores["azul"]}Número para investigar se é primo:{listaCores["limpar"]} '))
print(f'{listaCores["roxo"]}-=-{listaCores["limpar"]}'*12)
lista = []
lixeira = []
for a in range(1, primo+1, +1):
    if primo%a==0:
        lista.append(a)
    else:
        lixeira.append(a)
if len(lista)==2:
    print(f'{listaCores["verde"]}Número{listaCores["limpar"]} {primo} {listaCores["verde"]}É um número primo!{listaCores["limpar"]}')
    print('')
    print(f'{listaCores["verde"]}Número divisível apenas por{listaCores["limpar"]} {lista}.')
elif len(lista)>2:
    print(f'{listaCores["vermelho"]}Número{listaCores["limpar"]} {primo} {listaCores["vermelho"]}NÃO É um número primo!{listaCores["limpar"]}')
    print('')
    print(f'{listaCores["vermelho"]}Número divisível por{listaCores["limpar"]} {lista}')
print(f'{listaCores["roxo"]}-=-{listaCores["limpar"]}'*12)
