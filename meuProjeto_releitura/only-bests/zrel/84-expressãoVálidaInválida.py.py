lista= []
while True:
    expr = input('Expressão: ')
    if expr=='stop':
        break
    expl = list(expr)
    for a in expl:
        if a in ('(',')'):
            lista.append(a)
    if lista[-1]=='(':
        print('Expressão inválida!')
    elif lista[0]==')':
        print('Expressão inválida!')
    else:  
        for c in range(0, len(lista)):
            if lista[c]==')':
                if lista[:c+1].count('(')!=lista[:c+1].count(')'):
                    print('Expressão Inválida!')
                    break
                elif lista[:c+1].count('(')==lista[:c+1].count(')'):
                    if c==len(lista)-1:
                        print('Expressão Válida!')
    lista.clear()


'''     (a+b)()-()c-a()(      '''
