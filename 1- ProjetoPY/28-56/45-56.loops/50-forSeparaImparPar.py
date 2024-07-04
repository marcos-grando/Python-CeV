cont = 0
z = 0
lista = []
for a in range(1,6+1):
    quest = int(input(f'Digite {a}º número: '))
    if quest%2==0:
        lista.append(quest)
        z += quest
        cont += 1

print('-=-'*12)
if cont>=2:
    print(f'Dos {a} números digitados, {cont} eram pares {lista}.')
    print(f'A soma desses {cont} números resulta em {z}')
elif cont==1:
    print(f'Dos {a} números digitados, apenas {cont} número foi par {lista}.')
elif cont==0:
    print(f'Dos {a} números digitados nenhum foi par!')
print('-=-'*12)

'''
lixeira = []
    else:
        lixeira.append(quest)

'''


#print(lixeira)
#print(lista)
#print(z)
