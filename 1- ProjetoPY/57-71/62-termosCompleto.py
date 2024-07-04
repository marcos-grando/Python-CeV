# Melhorias do exerc "51-.py"

lista = []
termoInicial = int(input('Primeiro termo da Progressão Aritmética: '))
termos = int(input('Quantos termos da PA deseja saber: '))
razPA = int(input('Razão da Progressão Aritmética: '))

for a in range(termoInicial, termoInicial+(termos*razPA)+razPA, razPA):
    lista.append(a)
print('Progressão Aritmética: ')
print(lista[:termos])
print('-=-'*15)
while True:
    go = str(input('Deseja fazer uma nova operação? [s/n]: ')).lower()
    if go=='n' or go=='não' or go=='nao' or go=='no':
        print('-=--=--=--=- Operação Finalizada -=--=--=--=-')
        break
    if go=='s' or go=='sim' or go=='yes':      
        opt = int(input('''    [1] Alterar primeiro termo;
    [2] Alterar quantidade de termos;
    [3] Alterar a razão da PA;
    [4] Nova operação;
    [5] Finalizar.
    Opção desejada: '''))
        print('-=-'*15)
        if opt==1:
            termoInicial = int(input('Primeiro termo da Progressão Aritmética: '))
        if opt==2:
            termos = int(input('Quantos termos da PA deseja saber: '))
        if opt==3:
            razPA = int(input('Razão da Progressão Aritmética: '))
        if opt==4:
            termoInicial = int(input('Primeiro termo da Progressão Aritmética: '))
            termos = int(input('Quantos termos da PA deseja saber: '))
            razPA = int(input('Razão da Progressão Aritmética: '))
        if opt==5:
            print('-=-'*15)
            print('-=--=--=--=- Operação Finalizada -=--=--=--=-')
            break
        lista.clear()
        for a in range(termoInicial, termoInicial+(termos*razPA)+razPA, razPA):
            lista.append(a)
        print('Progressão Aritmética: ')
        print(lista[:termos])
        print('-=-'*15)
        

