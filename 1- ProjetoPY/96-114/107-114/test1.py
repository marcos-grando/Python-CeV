

while True:
    
    n = str(input('Dig: ')).replace(',','.').strip()
    if '-' in n[1:] or '+' in n[1:]:
        if '-' in n[1:] and '+' not in n[1:]:
            print('erro negativo')
        elif '+' in n[1:] and '-' not in n[1:]:
            print('erro positivo')
        else:
            print('Você colocou "+-" no meio dos números')
        print('..1')
