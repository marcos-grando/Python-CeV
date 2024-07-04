#1º versão - simplificada, import de funções: (dessa forma não precisa de math. toda vez que usar uma função)

from math import radians, sin, cos, tan 
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'No ângulo de {angulo}° temos:')
print(f'O SENO de {seno:.2f}!')
print(f'O COSSENO de {cosseno:.2f}!')
print(f'A TANGENTE de {tangente:.2f}!')

#2º versão - desnecessária, import todo módule:
'''
import math 
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'No ângulo de {angulo}° temos:')
print(f'O SENO de {seno:.2f}!')
print(f'O COSSENO de {cosseno:.2f}!')
print(f'A TANGENTE de {tangente:.2f}!')
'''