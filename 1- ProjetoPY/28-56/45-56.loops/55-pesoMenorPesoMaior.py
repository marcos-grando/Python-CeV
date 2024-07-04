#releitura do exercício 38-.py
print('-=-'*4)
pesos = []
for a in range(1, 5+1):
    pesos.append(int(input(f'Pesagem {a}: ')))
pesosOrdem = sorted(pesos)
print('-=-'*4)
print(f'Mais pesado: {pesosOrdem[-1]}')
print(f'Mais leve: {pesosOrdem[0]}')



'''
if num1>num2:
    print('O primeiro valor é o maior!')
elif num1<num2:
    print('O segundo valor é o maior!')
elif num1==num2:
    print('Ambos valores são iguais!')
'''
''' (opcional)
else: 
    print('Ambos valores são iguais!)
'''
