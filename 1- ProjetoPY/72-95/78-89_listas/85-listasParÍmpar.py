lista = [[],[]]
print('999 irá parar o programa!')

n=0
while True:
    n+=1
    num = int(input(f'{n}º número: '))
    if num==999:
        break
    elif num%2==0:
        lista[1].append(num)
    else:
        lista[0].append(num)

print(sorted(lista[0]))
print(sorted(lista[1]))