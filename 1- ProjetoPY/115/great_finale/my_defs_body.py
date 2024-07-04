from my_defs import head_title

def body_menuPrincipal():
    head_title('MENU PRINCIPAL')

def body_menuEscolha():
    while True:
        print(' '*4, '[1] Lista de convidados.')
        print(' '*4, '[2] Cadastrar convidado.')
        print(' '*4, '[3] Sair do Programa.')
        print('-'*37)
        escolha = (input('Opção desejada: ').strip())
        print('-'*37)
        if escolha not in ['1', '2', '3']:
            print('[Opção inválida!] Escolha uma das 3 opções: ')
        else:
            break
    return int(escolha)

def body_novoConvidado(arquivo_lista):
    from mydefs_package.lerNumber_mdl.defs_readn import readn_lerint
    from my_defs import head_dadosConfirmação, head_cadastrarConvidado

    while True:
        nome = input('Nome do convidado: ')
        idade = readn_lerint(f'Idade de {nome}: ')
        confere = head_dadosConfirmação(nome, idade)
        if confere==0:
            head_cadastrarConvidado(arquivo_lista, nome, idade)
            break
        while True:
            if confere==1:
                nome = input('Nome do convidado: ')
            elif confere==2:
                idade = readn_lerint(f'Idade de {nome}: ')
            else: 
                break
            confere = head_dadosConfirmação(nome, idade)
            if confere==0:
                head_cadastrarConvidado(arquivo_lista, nome, idade)
                break
        if confere==0: 
            break

def body_verConvidados(arquivo_lista):
    try:
        arquivo = open(arquivo_lista, 'rt')
    except:
        print('Erro ao abrir a lista de convidados! Tente mais tarde.')
    else:
        print(f'{'Lista de Convidados':^37}')
        print(' '*2, f'{'Nome':<25}', f'{'Idade'}')
        for linha in arquivo:
            dado = linha.split(',')
            dado[1] = dado[1].replace('\n', '')
            print(' '*2, f'{dado[0]:<25}', f'{f'{dado[1]} anos'}')
    finally:
        arquivo.close()

