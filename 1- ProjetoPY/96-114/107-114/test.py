





'''
valor = str(input(mensagem)).replace(',', '.').strip()
while valor.count('.')>1 or valor.replace(',','').replace('.','').isdigit()==False:
    valor = str(input(f'[ERRO] Apenas {mensagem.lower()}')).replace(',', '.').strip()
else: 
    return float(valor)
'''


'''
if n.replace('.','').replace(',','').isdigit()==True: print(n,'isnum')
else: print(n, 'nonum')

p = 'abc'
if 'a' in p and ('c' in p or 'b' in p): print('true')
'''