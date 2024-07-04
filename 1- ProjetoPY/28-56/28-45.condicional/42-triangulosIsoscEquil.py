print('Digite abaixo o valor das três retas do triângulo')
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segunda segmento: '))
r3 = int(input('Terceira segmento: '))


if r1<r2+r3 and r2<r1+r3 and r3<r1+r2: #exercício '35-formaTriângulo.py'
    print('Os segmentos aciam forma um triângulo ', end='')
    if r1==r2 and r2==r3 and r1==r3:   #if r1==r2==r3: (versão simplificada)
        print('Equilátero!')
    elif r1==r2 and r2!=r3 and r1!=r3: #if r1==r2!=r3!=r1: (versão simplificada)
        print('Isósceles!')
    elif r1!=r2 and r2!=r3 and r1!=r3: #if r1!=r2!=r3!=r1: (versão simplificada)
        print('Escaleno!')
else: 
    print('Triângulação negada!')




