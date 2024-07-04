tupla = (int(input('Digite número: ')), int(input('Digite número: ')), int(input('Digite número: ')), int(input('Digite número: ')))
print('')

print(f'Nº 9 foi repetido {tupla.count(9)}x')
if 3 in tupla:
    print(f'1º Nº 3 no {tupla.index(3)+1}º registro')
else:
    print(f'Sem Nº 3 registrado')
c=t=0
for p in range(0, len(tupla)):
    if tupla[p]%2==0:
        c+=1
if c>0:
    print(f'{c} Nºs pares')
if c==0:
    print('Nenhum Nº par')

