from time import sleep
def contador(a,b,c):
    from operator import neg
    if c==0:
        c=1
    if a<b:     #Ordem Crescente
        if c<0:
            c=neg(c)
        for cont in range(a,b+1,c):
            if cont<b:
                print(cont, end='-> ', flush=True)
                sleep(0.5)
            elif cont==b:
                print(cont)
    elif a>b:   #Ordem Decrescente
        if c>0:
            c=neg(c)
        for cont in range(a,b-1,c):
            if cont>b:
                print(cont, end='-> ', flush=True)
                sleep(0.5)
            if cont==b:
                print(cont)

print('--'*11)
contador(0,10,2)
sleep(1)

print('--'*11)
contador(10,0,-2)
sleep(1)

a = int(input('Início: '))
b = int(input('Final: '))
c = int(input('Contagem: '))
contador(a,b,c)