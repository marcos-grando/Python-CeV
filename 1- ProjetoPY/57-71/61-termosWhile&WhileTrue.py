# Melhorias do exerc "51-.py"

lista = []
termoInicial = int(input('Primeiro termo da Progressão Aritmética: '))
termos = int(input('Quantos termos da PA deseja saber: '))
razPA = int(input('Razão da Progressão Aritmética: '))
cont = 0

# com while:
while cont!=termos:
    lista.append(termoInicial)
    termoInicial += razPA
    cont += 1
print(lista)

# com while True: 
'''
while True:
    if cont==termos:
        break
    lista.append(termoInicial)
    termoInicial += razPA
    cont += 1
print(lista)
'''
