def readn_cleanNum(mensagem):
    número_inteiro = str(input(mensagem)).replace(',','.').strip()
    while número_inteiro.isdigit()==False:
        print('-'*34)
        if número_inteiro.count('.')>0 and '-' not in número_inteiro and '+' not in número_inteiro:
            print("Somente números, sem uso de pontuação!")
        elif número_inteiro.count('.')==0 and ('-' in número_inteiro or '+' in número_inteiro):
            print("Somente números, sem sinal de valor positivo/negativo!")
        elif número_inteiro.count('.')>0 and ('-' in número_inteiro or '+' in número_inteiro):
            print("Somente números, sem qualquer pontuação ou sinal de valor positivo/negativo")
        else:
            print('[ERRO] Digite apenas números!')
        print('-'*34)
        número_inteiro = str(input(f'{mensagem}')).replace(',','.').strip()
    else:
        return int(número_inteiro)

def readn_lerint(mensagem):
    número_inteiro = str(input(mensagem)).replace(',','.').strip()
    while número_inteiro.replace('-','').replace('+','').replace('.','').isdigit()==False:
        print('-'*49, '\n[ERRO] Digite um número inteiro válido.\n', '-'*48)
        número_inteiro = str(input(f'[2] {mensagem}')).replace(',','.').strip()
    while número_inteiro.count('.')>0 or ('+' in número_inteiro[1:] or '-' in número_inteiro[1:]):
        if número_inteiro.count('.')>0 and ('+' not in número_inteiro[1:] and '-' not in número_inteiro[1:]):
            print('-'*49, "\n[ERRO] Digite *apenas* números inteiros!\n", '-'*48)    
        elif ('+' in número_inteiro[1:] or '-' in número_inteiro[1:]) and número_inteiro.count('.')==0:
            if '+' in número_inteiro[1:] and '-' not in número_inteiro[1:]:
                print('-'*49, "\n[ERRO] Use '+' *somente* no início para indicar um número inteiro positivo (opcional).\n", '-'*48)
            elif '+' not in número_inteiro[1:] and '-' in número_inteiro[1:]:
                print('-'*49, "\n[ERRO] Use '-' *somente* no início para indicar um número inteiro negativo.\n", '-'*48)
            else:
                print('-'*49, "\n[ERRO] Use '+' (opcional) ou '-' *somente* para indicar um número inteiro positivo ou negativo.\n", '-'*48)
        else:
            print('-'*49, "\n[ERRO] Digite *apenas* números inteiros. Use '+' (opcional) ou '-' *somente* para indicar um número positivo ou negativo.\n", '-'*48)
        número_inteiro = str(input(f'[3] {mensagem}')).replace(',','.').strip()
        while número_inteiro.replace('-','').replace('+','').replace('.','').isdigit()==False:
            print('-'*49, '\n[ERRO] Digite um número inteiro válido.\n', '-'*48)
            número_inteiro = str(input(f'[4] {mensagem}')).replace(',','.').strip()
    else:
        return int(número_inteiro)

def readn_lerfloat(mensagem):
    número_decimal = str(input(mensagem)).replace(',','.').strip()
    while número_decimal.replace('-','').replace('+','').replace('.','').isdigit()==False:
        print('-'*49, '\n[ERRO] Digite um número decimal válido.\n','-'*48)
        número_decimal = str(input(f'[2] {mensagem}')).replace(',','.').strip()
    while número_decimal.count('.')>1 or ('+' in número_decimal[1:] or '-' in número_decimal[1:]):
        if número_decimal.count('.')>1 and ('+' not in número_decimal[1:] and '-' not in número_decimal[1:]):    #se +1 '.' e '+-' não está no meio de números
            print('-'*49, "\n[ERRO] Use '.' ou ',' *somente* para determinar o valor da casa decimal!\n", '-'*48)
        elif ('+' in número_decimal[1:] or '-' in número_decimal[1:]) and número_decimal.count('.')<=1:         #se '+-' está no meio de números e 1 ou menos '.'
            if '-' in número_decimal[1:] and '+' not in número_decimal[1:]: 
                print('-'*49, "\n[ERRO] Use '-' *apenas* no início para indicar um número negativo!\n", '-'*48)
            elif '+' in número_decimal[1:] and '-' not in número_decimal[1:]:
                print('-'*49, "\n[ERRO] Use '+' *apenas* no início para indicar um número positivo (opcional)!\n", '-'*48)
            else:
                print('-'*49, "\n[ERRO] Use '-' ou '+' (opcional) *apenas* no início para indicar um número negativo ou positivo!\n", '-'*48)
        else: 
            print('-'*49, "\n[ERRO] Use '-' ou '+' *apenas* no início para indicar negativo/positivo. E '.' ou ',' *somente* para determinar o valor da casa decimal.\n", '-'*48)       
        número_decimal = str(input(f'[3] {mensagem}')).replace(',','.').strip()
        while número_decimal.replace('-','').replace('+','').replace('.','').isdigit()==False:
            print('-'*49, '\n[ERRO] Digite um número decimal válido.\n', '-'*48)
            número_decimal = str(input(f'[4] {mensagem}')).replace(',','.').strip()  
    else:
        if '.' in número_decimal[0]:
            número_decimal = '0'+número_decimal
            return float(número_decimal)
        else:
            return float(número_decimal)

def test():
    print('test')


#while True:
    #print(readn_cleanNum('Digite num: '))

#while True:
    #print(readn_lerint('Valor númerico: '))    # para testar erros --> 46aabc ; 4,5 ; 4.5 ; .7 ; ,8 ; 4- ; 4+ ; 4+7 ; 4-7 ; 4-+ ; -+8 ; +-8

#while True:
    #print(readn_lerfloat('Valor númerico: '))  # para testar erros --> 46abc ; 4,,5 ; 4..8 ; 5,.7 ; ,-4 ; 4-7 ; 4+6 ; 46+ ; 47- ; 6-+ ; +-5 ; -+5
