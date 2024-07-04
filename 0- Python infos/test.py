from mydefs_package.defsGood_mdl.defsGood import loading_, arrasta_pLadoTxt
from mydefs_package.mycores_mdl.mycores import bold_, undl_, neutro_, cor_bold
from time import sleep
from mydefs_package.formatime_mdl.formatime import head_timeTitle

print(' '*7, end='')
arrasta_pLadoTxt('[  GO!  ]', True, 7, 4, 4, 1, 0.035)

print(' '*13, end='')
head_timeTitle(bold_('JO',1), False)
sleep(0.5)
head_timeTitle(bold_('-KEN',2), False)
sleep(0.5)
head_timeTitle(bold_('-PÔ', 6), True)

'''
if (vendas:=int(input('Número de vendas: '))) >= 1000:
    bonus = 0.05 * (vendas-1000)
else:
    bonus = 0
print(f'Ganhou {bonus}')

vendas = int(inpout('Número de vendas: '))
if vendas >= 1000:
    bonus = 0.05*(vendas-1000)
else:
    bonus = 0
print('Ganhou {bonus}')
'''

'''
valores = [int(val) for val in x]

x = ['123', '456', '789']
valores = []
for val in x:
    valores.append(int(val))
'''    