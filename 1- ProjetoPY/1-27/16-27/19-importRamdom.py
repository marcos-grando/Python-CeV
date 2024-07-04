from random import choice

print('Sorteio? Que sorteio? Seja bem vindo ao sorteiação!!')

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
listaAlunos = [nome1, nome2, nome3, nome4]  # var=[] cria uma lista com o que for digitar dentro
sorteioAluno = choice(listaAlunos)   #random.choice(listaAlunos) = 'escolha' 'randomizada' dentro da 'lista de alunos'

print(f'O sorteado foi.....o aluno {sorteioAluno}!!')


