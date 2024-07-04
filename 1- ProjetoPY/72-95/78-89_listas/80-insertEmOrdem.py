lista = []

print('Digite 10 números')
for n in range(0, 10):
    num = int(input(f'{n+1}º número: '))
    nO = sorted(lista)
    if n==0 or num<nO[0]:
        lista.insert(0, num)
        print('Adicionado no início!')
    elif n==0 or num>nO[-1]:
        lista.append(num)
        print('Adicionado no final!')
    else:
        a=0
        while num>nO[a]: #enqto num for maior que lista[a], a aumenta 1 R->  4
            a+=1          
        lista.insert(a, num)
        print(f'Adicionado na {a+1}º posição !')
print(lista)

'''
5 7 8 9 4 5 6 7 8 1 5 4

4 5 7 8 9

  1   2  3  4  5  5  5  5  5  7  8  9  10 11 15
  0   1  2  3  4  5  6  7  8  9  10 11 12 13 14
              -11-10-9 -8 -7 -6  -5 -4 -3 -2 -1  

        while not num>lista[b]: #enqto num não for maior que lista[b], b diminui 1 R-> -7
            b-=1
        c = (a+b)/2 #10 ou 12 / 5 ou 6 
'''