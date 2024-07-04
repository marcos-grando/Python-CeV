times = ('botafogo', 'Atlético-MG', 'Bragantino', 'Atlético-PR', 'Bahia', 'Internacional', 'Crcuzeiro', 'Flamengo',
        'Grêmio', 'Criciúma', 'Fortaleza', 'Palmeiras', 'Juventude', 'São Paulo', 'Corinthians', 
        'Fluminense', 'Vasco da Gama', 'Vitória', 'Atlético-GO', 'Cuiabá')

while True:
    print('='*27)
    opt = str(input('[a] 5 primeiros\n[b] 4 últimos\n[c] Ordem Alfabética\n[d] Kd Grêmio?\n[p] Parar \nOpção desejada: '))
    print('='*27)
    if opt=='a':
        for time in range(0,5):
            print(f'{time+1}º - {times[time]}')
    if opt=='b':    
        cont=1
        for last in range(0, 20):
            if times[last]==times[-1] or times[last]==times[-2] or times[last]==times[-3] or times[last]==times[-4]:
                print(f'{cont}º - {times[last]}')
            cont+=1
    if opt=='c':
        ordAlf = sorted(times)
        for c in range(0,20):
            print(f'{ordAlf[c]} em {times.index(ordAlf[c])+1}')
    if opt=='d':
        cont1=0
        while times[cont1]!='Grêmio':
            cont1+=1
        print(f'Grêmio está em {times.index('Grêmio')+1}º lugar')
    if opt=='p':
        break
    