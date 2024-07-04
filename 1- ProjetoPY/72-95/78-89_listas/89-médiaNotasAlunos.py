
listaA = ['Marcos', 'Nelóg', 'Senku']
listaN = [[4,6], [7,9], [4,8]]
'''
listaA = []
listaN = []
''''''
print("'stop' pra parar!")
while True:
    print('--'*9)
    nome = str(input('Aluno: ')).title().strip()
    while nome in listaA:
        print('[ERRO] Nome já cadastrado!')
        nome = str(input('Aluno: ')).title().strip()
    if nome.lower()=='stop':
        break
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    listaA.append(nome)
    listaN.append([nota1, nota2])
'''
print('-='*18)
print('NOME      MÉDIA')
print('--'*9)
for n in range(0, len(listaA)):
    print(f'{listaA[n]:<10}', end='')
    print(f'{(listaN[n][0]+listaN[n][1])/2}')
print('-='*18)
while True:
    aluno = str(input("Mostrar nota do aluno: ['stop' pra encerrar]: ")).title().strip()
    if aluno=='stop':
        break
    while aluno not in listaA:
        aluno = str(input("[ERRO] Aluno não encontrado! Digite o nome corretamente: ")).title().strip()
    post = listaA.index(aluno)
    print(f'Notas de {listaA[listaA.index(aluno)]}: ', end='')
    print(f'{listaN[listaA.index(aluno)][0]:.1f} e {listaN[listaA.index(aluno)][1]:.1f} !')