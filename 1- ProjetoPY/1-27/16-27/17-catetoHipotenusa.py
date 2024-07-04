#1º versão - lógica aritmética:
catetoA = float(input('Valor do cateto oposto: '))
catetoB = float(input('Valor do cateto adjacente: '))
hipotenusa = ((catetoA**2)+(catetoB**2))**(1/2)

print(f'A hipotenusa desse triângulo retângulo é {hipotenusa:.3f}!')

#2º versão - utilizando math.hypot():
'''
from math import hypot 
catetoA = float(input('Valor do cateto oposto: '))
catetoB = float(input('Valor do cateto adjacente: '))
hipotenusa = math.hypot(catetoA, catetoB)

print(f'A hipotenusa desse triângulo retângulo é {hipotenusa:.3f}!')
'''
