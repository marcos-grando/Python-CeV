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
        print('Expressão inválida!1')
    elif lista[0]==')':
        print('Expressão inválida!2')
    else:  
        for c in range(0, len(lista)):
            if lista[c]==')':
                if lista[:c+1].count('(')==lista[:c+1].count(')'):
                    if c==len(lista)-1:
                        print('Expressão Válida!')                
                if lista[:c+1].count('(')<lista[:c+1].count(')'):
                    print('Expressão Inválida!3')
                    break
                if lista[:c+1].count('(')>lista[:c+1].count(')'):
                    print('Expressão Inválida!4')
                    break
    lista.clear()

'''Jeito mais eficiência, aula referências:'''
'''
lista1 = []
for b in expl:
    if b in('('):
        lista1.append(b)
    elif b in(')'):
        if len(lista1)>0:
            lista1.pop()
        else:
            lista1.append(')')
            break
if len(lista1)==0:
    print('Expressão válida!')
elif len(lista1)!=0:
    print('Expressão inválida!')
'''