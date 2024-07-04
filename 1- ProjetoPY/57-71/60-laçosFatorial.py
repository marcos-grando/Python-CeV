# Usando 'for'

numero = int(input("Fatorial de: "))

for f in range(numero-1, 0, -1):
    numero *= f
    print(f'{numero}', end='')
    print(' x ' if f>1 else ' = ', end='')
print(numero)

# Usando 'while'
'''
numero = int(input("Fatorial de: "))
numero2 = int(numero-1)

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1
print(resultado)
'''

# Usando 'while True'
'''
numero = int(input("Fatorial de: "))
numero2 = int(numero-1)

while True:
    print(f'{numero2+1}', end='')
    numero *= numero2 
    numero2 -= 1
    print(f' x ' if numero2>0 else ' x 1 = ', end='')
    if numero2==0:
        break
print(numero)
'''
