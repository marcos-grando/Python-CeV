def money_moeda(valor, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')

def money_metade(número, ismoeda=False):
    número = número/2
    return número if ismoeda==False else money_moeda(número)

def money_dobro(número, ismoeda=False):
    número = número*2
    return número if ismoeda==False else money_moeda(número)

def money_aumentar(número, porcentagem=0, ismoeda=False):
    porcentagem = porcentagem/100
    número = número + (número*porcentagem)
    return número if ismoeda==False else money_moeda(número)

def money_diminuir(número, porcentagem=0, ismoeda=False):
    porcentagem = porcentagem/100
    número = número - (número*porcentagem)
    return número if ismoeda==False else money_moeda(número)

def money_resumo(valor, porcentagem_aumento, porcentagem_redução):
    a= 20
    b= 0
    print('-'*31)
    print(f'{f'RESUMO DO VALOR':^31}')
    print('-'*31)

    print(f'{f'Preço analisado:':<{a}}', end='') 
    print(f'{money_moeda(valor):<{b}}')
    print(f'{f'Dobro do preço:':<{a}}', end='')
    print(f'{money_dobro(valor, True):<{b}}')
    print(f'{f'Metade do preço:':<{a}}', end='')
    print(f'{money_metade(valor, True):<{b}}')
    print(f'{f'{porcentagem_aumento}% de aumento:':<{a}}', end='')
    print(f'{money_aumentar(valor, porcentagem_aumento, True):<{b}}')
    print(f'{f'{porcentagem_redução}% de redução:':<{a}}', end='')
    print(f'{money_diminuir(valor, porcentagem_redução, True):<{b}}')
    
    print('-'*31)

def money_lerMoeda(mensagem):
    valor = str(input(mensagem)).replace(',', '.').strip()
    while valor.count('.')>1 or valor.replace(',','').replace('.','').isdigit()==False:
        valor = str(input(f'[ERRO] Apenas {mensagem.lower()}')).replace(',', '.').strip()
    else: 
        return float(valor)

while True:
    print(money_lerMoeda('d: '))