
lista = []
termoInicial = int(input('Primeiro termo da Progressão Aritmética: '))
termos = int(input('Quantos termos da PA deseja saber: '))
razPA = int(input('Razão da Progressão Aritmética: '))

for a in range(termoInicial, termoInicial+(termos*razPA)+razPA, razPA):
    lista.append(a)
print(lista[:termos])
print(lista)


