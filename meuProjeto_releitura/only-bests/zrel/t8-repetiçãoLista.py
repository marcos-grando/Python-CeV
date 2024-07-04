#Usando LISTAS com repetição:
n = []
for c in range(0,3):
    n.append(int(input('Digite: ')))    #Repete a pergunta 3x e adicina cada resposta como valores na lista
print(f'''Você escolheu:
    Começar na casa {n[0]}
    Terminar na casa {n[1]}
    E {n[2]} passo de cada vez!''')
for d in range(n[0], n[1]+1, n[2]):     #Os valores da lista, escolhido pelo usuário, se tornam instruções
    print(f'Passo {d} --> ', end='')
print('Fim')