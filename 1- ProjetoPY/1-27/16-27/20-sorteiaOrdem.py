from random import sample

nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
listaSorteio = sample(lista, 4)  #sample="amostre", ou sejam ramdom.sample(lista)='amostre' de forma 'randômica' a 'lista'

print(f'A ordem de apresentação será: {listaSorteio}!')






