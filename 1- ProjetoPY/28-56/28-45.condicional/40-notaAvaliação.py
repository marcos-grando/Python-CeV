print('Programa para calcular se seu aluno foi aprovado ou reprovado!')
print('Apresente notas das avaliaçãos de seu aluno abaixo:')

aluno = input('Nome do aluno(a): ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = float((nota1+nota2+nota3)/3)

if media<5.0:
    print(f'Sua média foi de {media:.2f}.')
    print(f'Aluno(a) {aluno}: REPROVADO(A)!')
elif 5.0<=media<7.0:
    print(f'Sua média foi de {media:.2f}.')
    print(f'Aluno(a) {aluno}: EM RECUPERAÇÃO!')
elif media>=7.0:
    print(f'Sua média foi de {media:.2f}.')
    print(f'Aluno(a) {aluno}: APROVADO(A)!')