from mydefs_package.lerNumber_mdl.defs_readn import readn_lerint
from my_defs_body import body_menuEscolha, body_listaConvidados, body_novoConvidado, body_removerAlterar
from my_defs import head_title

print('='*37,'\n', f'{'SISTEMA DE CONVIDADOS v1.12.2':^35}')
while True:
    head_title('MENU PRINCIPAL')
    escolha = body_menuEscolha()
    if escolha==1:
        body_listaConvidados()
        print('-'*37)
        print('[1] Mostrar menu | [2] Fechar sistema')
        continuar = input('Opção desejada: ')
        if continuar=='1':
            continue
        elif continuar=='2':
            print('='*37, '\n', f'{'Programa finalizado  ':^37}')
            print('='*37)
            break
    elif escolha==2:
        body_novoConvidado()
    elif escolha==3:
        body_removerAlterar()
    elif escolha==4:
        print('='*37, '\n', f'{'Programa finalizado  ':^37}')
        print('='*37)
        break
