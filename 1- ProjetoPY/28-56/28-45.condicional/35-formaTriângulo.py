print('-=-'*20)
print('Analisarei o teu triângulo!!')
print('-=-'*20)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('Você foi triângulado!')
else:
    print('Triângulação negada!')


'''
Resumidamente, se uma única reta for maior que a soma das outras duas
então não há como formar um triângulo.
'''

