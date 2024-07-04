from my_defs import head_title, head_printErro


def body_menuEscolha():
    while True:
        print(' '*4, '[1] Lista de convidados.')
        print(' '*4, '[2] Cadastrar convidado.')
        print(' '*4, '[3] Remover/alterar dados.')
        print(' '*4, '[4] Sair do Programa.')
        print('-'*37)
        escolha = input('Opção desejada: ').strip()
        print('-'*37)
        if escolha not in ['1', '2', '3', '4']:
            print('[Opção inválida!] Escolha uma das 3 opções: ')
        else:
            break
    return int(escolha)


def body_listaConvidados():
    from my_defs import head_verConvidados

    print(f'{'Lista de Convidados':^37}')
    print(f'{'Nºs':<4}', f'{'Nome':<25}', f'{'Idade'}')

    listaConvidados = head_verConvidados()
    for convidado in listaConvidados:
        id = convidado[0]
        nome = convidado[1]
        idade = convidado[2]
        print(' ' f'{id:<3}', f'{nome:<25}', f'{f'{idade} anos'}')


def body_novoConvidado():
    from mydefs_package.lerNumber_mdl.defs_readn import readn_lerint
    from my_defs import head_dadosConfirmação, head_cadastrarConvidado

    while True:
        nome = input('Nome do convidado: ')
        idade = readn_lerint(f'Idade de {nome}: ')
        confere = head_dadosConfirmação(nome, idade)
        if confere==0:
            head_cadastrarConvidado(nome, idade)
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
                head_cadastrarConvidado(nome, idade)
                break
        if confere==0: 
            break


def body_excluirConvidado():
    from my_defs import head_validarN, head_identificarConvidado, head_excluirConvidado, head_reorganizaOrdem

    print('Escreva o número do convidado que você deseja excluir da lista')
    nConv = input('Nº: ')
    excluir = head_validarN(nConv)

    while excluir==False:
        print('Convidado não encontrado na lista. Tentar novamente?')
        tentar = input('[1] Sim | [2] Voltar | Opção desejada: ')
        while tentar not in ['1', '2']:
            print(f'Opção "{tentar}" inexistente. Tentar novamente?')
            tentar = input('[1] Sim | [2] Voltar | Opção desejada: ')

        if tentar=='1':
            nConv = input('Nº do convidado: ')
            excluir = head_validarN(nConv)
        elif tentar=='2':
            break
    else:
        convidado = head_identificarConvidado(nConv)
        print(f'Você quer excluir {convidado[1]}, de {convidado[2]} anos, da lista?')
        confirmar = input('[1] Sim | [2] Não | Opção desejada: ')
        if confirmar=='1':
                head_excluirConvidado(nConv)
                head_reorganizaOrdem()
                print(f'[1] Fazer outra alteração | [2] Voltar ao menu')
        else: 
            print(f'Nenhum convidado foi excluído.')
            print(f'[1] Fazer alteração | [2] Voltar ao menu')
        continuar = input('Opção desejada: ')
        while continuar not in ['1', '2']:
            print(f'Opção {continuar} inválida! Tente novamente.')
            continuar = input('Opção desejada: ')
        else:
            if continuar=='1':
                return False
            else:
                return True


def body_menuRemoverAlterar():
    head_title('REMOVER/ALTERAR')
    print('Qual alteração deseja realizar?')
    print(' '*4, '[1] Alterar dados')
    print(' '*4, '[2] Remover convidado')
    print(' '*4, '[3] Ver lista de convidados')
    print(' '*4, '[4] Voltar ao Menu')
    cud = input('Opção desejada: ')
    while cud not in ['1', '2', '3', '4']:
        head_printErro(f'Opção "{cud}" inválida! Tente novamente.')
        cud = input('Opção desejada: ')
    print('-'*37)

    return cud


def body_removerAlterar():
    from my_defs_body import body_listaConvidados, body_excluirConvidado, body_alterarDados, head_printErro

    while True:
        cud = body_menuRemoverAlterar()

        if cud=='1':
            fim = body_alterarDados()
        elif cud=='2':
            fim = body_excluirConvidado()
        elif cud=='3':
            body_listaConvidados()
            print('-'*37)
            print('Realizar alguma alteração?')
            confirmar = input('[1] Sim | [2] Voltar | Opção desejada: ')
            while confirmar not in ['1', '2']:
                print(f'Opção {confirmar} inválida! Tente novamente!')
                print('Realizar alteração?')
                confirmar = input('[1] Sim | [2] Menu | Opção desejada: ')
            print('-'*37)
            if confirmar=='2':
                break
            else:
                continue
        elif cud=='4':
            return
        
        if fim==True:
            return
        else:
            continue


def body_alterarDados():
    from my_defs import head_validarN, head_identificarConvidado, head_alterarCadastro

    while True:
        print('Quais informações deseja alterar?')
        print(' '*4, '[1] Alterar nome')
        print(' '*4, '[2] Alterar idade')
        print(' '*4, '[3] Alterar Ambos')
        print(' '*4, '[4] Voltar')
        opt = input(f'Opção desejada: ')
        while opt not in ['1', '2', '3', '4']:
            head_printErro(f'Opção "{opt}" inválida! Tente novamente.')
            opt = input(f'Opção desejada: ')
        else:
            opt = int(opt)
        
        if opt==4:
            return False
        elif opt==3:
            print('Informe o número do convidado que você deseja fazer as alterações')
        elif opt==2:
            print('Informe o número do convidado que você deseja alterar a idade')
        elif opt==1:
            print('Informe o número do convidado que você deseja alterar o nome')
        nConv = input('Nº: ')
        alterar = head_validarN(nConv)
        while alterar==False:
            print('Convidado não encontrado na lista. Tentar novamente?')
            tentar = input('[1] Sim | [2] Voltar | Opção desejada: ')
            while tentar not in ['1', '2']:
                print(f'Opção "{tentar}" inexistente. Tentar novamente?')
                tentar = input('[1] Sim | [2] Voltar | Opção desejada: ')
            else:
                if tentar=='1':
                    nConv = input('Nº do convidado: ')
                    alterar = head_validarN(nConv)
                elif tentar=='2':
                    break
        else:
            convidado = head_identificarConvidado(nConv)
            nome = convidado[1]
            idade = convidado[2]
            nConv = int(nConv)

            if opt==1:
                print(f'Deseja alterar o nome de {nome}?')
            elif opt==2:
                print(f'Deseja alterar a idade de {nome}, {idade} anos?')
            elif opt==3:
                print(f'Deseja alterar os dados de {nome}, {idade} anos?')
            confirmar = input('[1] Sim | [2] Não | Opção desejada: ')
            while confirmar not in ['1', '2']:
                print(f'Opção {confirmar} inválida! Tente novamente.')
                confirmar = input('Opção desejada: ')
            else:
                if confirmar=='1':
                    if opt==1:
                        nome = input('Cadastre novo nome: ')
                    elif opt==2:
                        idade = input('Cadastre nova idade: ')
                    elif opt==3:
                        nome = input('Cadastre novo nome: ')
                        idade = input('Cadastre nova idade: ')
                    head_alterarCadastro(opt, nConv, nome, idade)
                    print(f'[1] Fazer outra alteração | [2] Voltar ao menu')
                else:
                    print('-'*37)
                    print(f'Nenhuma alteração feita.')
                    print('-'*37)
                    print(f'[1] Remover/Alterar | [2] Voltar ao menu')
                continuar = input('Opção desejada: ')
                while continuar not in ['1', '2']:
                    print(f'Opção {continuar} inválida! Tente novamente.')
                    continuar = input('Opção desejada: ')
                else:
                    if continuar=='1':
                        return False
                    else:
                        return True

