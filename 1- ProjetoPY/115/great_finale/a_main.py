from mydefs_package.lerNumber_mdl.defs_readn import readn_lerint
from my_defs_body import *
from my_defs import *

arquivo = 'c:/Users/marco/Desktop/Python bro/1- ProjetoPY/115/great_finale/banco_dados.txt'
           
print('='*37,'\n', f'{'SISTEMA DE CONVIDADOS v1.12.2':^35}')
while True:
    body_menuPrincipal()
    escolha = body_menuEscolha()
    if escolha==1:
        body_verConvidados(arquivo)
    elif escolha==2:
        body_novoConvidado(arquivo)
    elif escolha==3:
        print('='*37, f'{'\nPrograma finalizado':^37}')
        print('='*37)
        break
