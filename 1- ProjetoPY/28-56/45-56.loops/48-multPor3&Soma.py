num = int(input('Num: '))
num2 = int(input('Num: '))
cont = 0
z = 0
lista = []
for a in range(num, num2+1):
    if a%2==1 and a%3==0:
        lista.append(int(a))
        z += a 
        cont += 1
print('')
print(f'Abaixo a lista de números ímpares múltiplos por 3.')
print(lista)
print('')
print(f'A soma desses {cont} números dá: {z}')