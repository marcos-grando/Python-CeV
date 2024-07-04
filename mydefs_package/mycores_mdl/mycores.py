#   LISTA DE CORES 1v
#none:
def cor_nat(cor='limpar'):
    if cor==0:
        co_0 = '\033[30m' # preto
        return co_0
    elif cor==1:
        co_1 = '\033[31m' # vermelho
        return co_1
    elif cor==2:
        co_2 = '\033[32m' # verde
        return co_2
    elif cor==3:
        co_3 = '\033[33m' # amarelo
        return co_3
    elif cor==4:
        co_4 = '\033[34m' # azul
        return co_4
    elif cor==5:
        co_5 = '\033[35m' # roxo
        return co_5
    elif cor==6:
        co_6 = '\033[36m' # ciano
        return co_6
    elif cor==7:
        co_7 = '\033[37m' # cinza
        return co_7
    elif cor==8:
        co_8 = '\033[97m' # branco
        return co_8
    elif cor=='limpar':
        c_cl = '\033[m'
        return c_cl
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print("Opção automática: cor='limpar' -> limpar cor")
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#bold:
def cor_bold(cor='limpar'):         
    if cor==0:
        bold_0 = '\033[1;30m' # preto
        return bold_0
    elif cor==1:
        bold_1 = '\033[1;31m' # vermelho
        return bold_1
    elif cor==2:
        bold_2 = '\033[1;32m' # verde
        return bold_2
    elif cor==3:
        bold_3 = '\033[1;33m' # amarelo
        return bold_3
    elif cor==4:
        bold_4 = '\033[1;34m' # azul
        return bold_4
    elif cor==5:
        bold_5 = '\033[1;35m' # roxo  
        return bold_5
    elif cor==6:
        bold_6 = '\033[1;36m' # ciano
        return bold_6
    elif cor==7:
        bold_7 = '\033[1;37m' # cinza
        return bold_7
    elif cor==8:
        bold_8 = '\033[1;97m' # branco
        return bold_8
    elif cor=='limpar':
        c_cl = '\033[m'
        return c_cl
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print("Opção automática: cor='limpar' -> limpa a cor")
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#underline:
def cor_undl(cor='limpar'):
    if cor==0:
        undl_0 = '\033[4;30m' # preto
        return undl_0
    elif cor==1:
        undl_1 = '\033[4;31m' # vermelho
        return undl_1
    elif cor==2:
        undl_2 = '\033[4;32m' # verde
        return undl_2
    elif cor==3:
        undl_3 = '\033[4;33m' # amarelo
        return undl_3
    elif cor==4:
        undl_4 = '\033[4;34m' # azul
        return undl_4
    elif cor==5:
        undl_5 = '\033[4;35m' # roxo
        return undl_5
    elif cor==6:
        undl_6 = '\033[4;36m' # ciano
        return undl_6
    elif cor==7:
        undl_7 = '\033[4;37m' # cinza
        return undl_7
    elif cor==8:
        undl_8 = '\033[4;38m' # branco
        return undl_8
    elif cor=='limpar':
        c_cl = '\033[m'
        return c_cl
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print("Opção automática: cor='limpar' -> limpa a cor")
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#testes
def test_cor(tipo):
    if tipo==1 or tipo=='co':
        for cores in range(0,9):
            print(f'{cor_nat(cores)}Uma ameixa numa cesta.{cor_nat()}')
    
    elif tipo==2 or tipo=='bold':
        for cores in range(0,9):
            print(f'{cor_bold(cores)}Uma ameixa numa cesta.{cor_bold()}')

    elif tipo==3 or tipo=='underline' or tipo=='undl':
        for cores in range(0,9):
            print(f'{cor_undl(cores)}Uma ameixa numa cesta.{cor_undl()}')
    else:
        print('tenta certo')

# print(f'Uma {cor_bold(5)}ameixa{cor_bold()} numa {cor_bold(3)}cesta{cor_bold()}')

#   LISTA DE CORES 2v
#none:
def neutro_(mensagem, cor=0):   #0
    if cor==0:
        texto_preto = f'\033[30m{mensagem}\033[m'
        return texto_preto
    elif cor==1:
        texto_vermelho = f'\033[31m{mensagem}\033[m'
        return texto_vermelho
    elif cor==2:
        texto_verde = f'\033[32m{mensagem}\033[m'
        return texto_verde
    elif cor==3:
        texto_amarelo = f'\033[33m{mensagem}\033[m'
        return texto_amarelo
    elif cor==4:
        texto_azul = f'\033[34m{mensagem}\033[m'
        return texto_azul
    elif cor==5:
        texto_roxo = f'\033[35m{mensagem}\033[m'
        return texto_roxo
    elif cor==6:
        texto_ciano = f'\033[36m{mensagem}\033[m'
        return texto_ciano
    elif cor==7:
        texto_cinza = f'\033[37m{mensagem}\033[m'
        return texto_cinza
    elif cor==8:
        texto_branco = f'\033[97m{mensagem}\033[m'
        return texto_branco
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#bold:
def bold_(mensagem, cor=0):     #1
    if cor==0:
        texto_preto = f'\033[1;30m{mensagem}\033[m'
        return texto_preto
    elif cor==1:
        texto_vermelho = f'\033[1;31m{mensagem}\033[m'
        return texto_vermelho
    elif cor==2:
        texto_verde = f'\033[1;32m{mensagem}\033[m'
        return texto_verde
    elif cor==3:
        texto_amarelo = f'\033[1;33m{mensagem}\033[m'
        return texto_amarelo
    elif cor==4:
        texto_azul = f'\033[1;34m{mensagem}\033[m'
        return texto_azul
    elif cor==5:
        texto_roxo = f'\033[1;35m{mensagem}\033[m'
        return texto_roxo
    elif cor==6:
        texto_ciano = f'\033[1;36m{mensagem}\033[m'
        return texto_ciano
    elif cor==7:
        texto_cinza = f'\033[1;37m{mensagem}\033[m'
        return texto_cinza
    elif cor==8:
        texto_branco = f'\033[1;97m{mensagem}\033[m'
        return texto_branco
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#underline:
def undl_(mensagem, cor=0):     #2
    if cor==0:
        texto_preto = f'\033[4;30m{mensagem}\033[m'
        return texto_preto
    elif cor==1:
        texto_vermelho = f'\033[4;31m{mensagem}\033[m'
        return texto_vermelho
    elif cor==2:
        texto_verde = f'\033[4;32m{mensagem}\033[m'
        return texto_verde
    elif cor==3:
        texto_amarelo = f'\033[4;33m{mensagem}\033[m'
        return texto_amarelo
    elif cor==4:
        texto_azul = f'\033[4;34m{mensagem}\033[m'
        return texto_azul
    elif cor==5:
        texto_roxo = f'\033[4;35m{mensagem}\033[m'
        return texto_roxo
    elif cor==6:
        texto_ciano = f'\033[4;36m{mensagem}\033[m'
        return texto_ciano
    elif cor==7:
        texto_cinza = f'\033[4;37m{mensagem}\033[m'
        return texto_cinza
    elif cor==8:
        texto_branco = f'\033[4;97m{mensagem}\033[m'
        return texto_branco
    else:
        print('-'*57)
        print('[Opção inválida] Lista de opções abaixo:')
        print('cor=0 -> preto   | cor=1 -> vermelho | cor=2 -> verde  |')
        print('cor=3 -> amarelo | cor=4 -> azul     | cor=5 -> roxo   |')
        print('cor=6 -> ciano   | cor=7 -> cinza    | cor=8 -> branco |')
        print('-'*57)

#testes
def test_(mensagem, test):
    if test==0 or test=='neutro':
        for cores in range(0,9):
            print(f'{neutro_(mensagem, cores)}')
    elif test==1 or test=='bold':
        for cores in range(0,9):
            print(f'{bold_(mensagem, cores)}')
    elif test==2 or test=='undl' or test=='underline':
        for cores in range(0,9):
            print(f'{undl_(mensagem, cores)}')
    elif test==3:
        for cores in range(0,9):
            print(f'{neutro_(mensagem, cores)}', end=' | ')
            print(f'{bold_(mensagem, cores)}', end=' | ')
            print(f'{undl_(mensagem, cores)}')
    else:
        print('Seilá notok')





