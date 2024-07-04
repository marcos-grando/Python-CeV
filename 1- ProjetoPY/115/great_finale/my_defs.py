def head_title(mensagem):
    print('='*37)
    print(f'{f'{mensagem}':^37}')
    print('-'*37)

def head_idadeCerta(mensagem):
    idade_certa = input(mensagem).strip()
    while idade_certa.isdigit==False:
        print('[ERRO] Digite a idade corretamente.')
        idade_certa = input(mensagem).strip()
    return int(idade_certa)

def head_printErro(mensagem):
    """
    Apenas para usar com 'dados_confirmação()'
    """
    print('-'*49)
    print(mensagem)
    print('-'*49)

def head_dadosConfirmação(nome, idade):
    dados_corretos = input(f'Você cadastrou {nome} de {idade} anos. Confere?\n[1] Sim | [2] Não: ').strip()
    while dados_corretos not in ['1', '2']:
        head_printErro('Por favor, apenas confirme se os dados estão corretos!')
        dados_corretos = input('[1] Dados corretos | [2] Dados incorretos: ').strip()
    print('-'*49)
    if dados_corretos=='2':
        dados_incorretos = input('Qual informação está incorreta?\n[1] Nome | [2] Idade | [3] Ambas as informações: ').strip()
        while dados_incorretos not in ['1', '2', '3']:
            head_printErro('Por favor, digite apenas a informação incorreta!')
            dados_incorretos = input('[1] Nome | [2] Idade | [3] Nome & idade: ').strip()      
        else:
            print('-'*49)
            return int(dados_incorretos)
    else:
        dados_corretos = 0
        return int(dados_corretos)

def head_cadastrarConvidado(arquivo, nome='<não informado>', idade=0):
    try:
        lista_convidados = open(arquivo, 'at')
    except:
        print('Erro ao abrir a lista de convidados! Tente mais tarde.')
    else:
        try:
            lista_convidados.write(f'{nome},{idade}\n')
        except:
            print('Erro ao tentar fazer o cadastro! Tente mais tarde.')
        else:
            print(f'Cadastro de {nome}, {idade} anos, feito com sucesso.')
            lista_convidados.close()

