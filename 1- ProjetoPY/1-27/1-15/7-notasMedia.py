alunoNome = input('Nome do aluno: ')
primeiraNota = float(input('Nota da primeira prova: '))
segundaNota = float(input('Nota da segunda prova: '))
notaMedia = (primeiraNota+segundaNota)/2

print(f'O aluno {alunoNome} tirou {primeiraNota:.1f} em sua primeira prova e {segundaNota:.1f} em sua segunda prova, portanto sua média foi de {notaMedia:.1f}!')
