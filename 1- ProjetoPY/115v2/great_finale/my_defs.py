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


def head_conector():
    import mysql.connector
    conector = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql123',
        database='db_convidados'
    )
    return conector


def head_verConvidados():
    try:    #tentativa de acessar banco de dados do MySQL
        conector = head_conector()
    except:
        print('Erro ao conectar com o banco de dados "db_convidados" do MySQL')
    else:
        try:    #tentativa de fazer uma leitura de dados no MySQL
            cursor = conector.cursor()

            comando = f'select * from convidados;'
            cursor.execute(comando)
            resultado = cursor.fetchall()
        except:
            print('Erro ao tentar fazer a leitura desses dados em "db_convidados" do MySQL')
        else:
            cursor.close()
            conector.close()
            
            return resultado            


def head_cadastrarConvidado(nome='<não informado>', idade=0):
    try:    #tentativa de acessar banco de dados do MySQL
        conector = head_conector()
    except:
        print('Erro ao conectar com o banco de dados "db_convidados" do MySQL')
    else:
        try:    #tentativa de fazer uma inserção de dados no MySQL
            cursor = conector.cursor()

            cud = f'insert into convidados (nome, idade) values ("{nome}", "{idade}")'
            cursor.execute(cud)
            conector.commit()
        except:
            print('Erro ao tentar fazer a inserção desses dados em "db_convidados" do MySQL')
        else:
            print(f'Cadastro de {nome}, {idade} anos, feito com sucesso.')
            cursor.close()
            conector.close()


def head_validarN(n_convidado):
    conector = head_conector()

    cursor = conector.cursor()

    comando = f'select id from convidados;'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    for n in resultado:
        if n[0]==int(n_convidado):
            fim=True
            break
        else:
            fim=False

    cursor.close()
    conector.close()

    return fim


def head_identificarConvidado(n_convidado):
    conector = head_conector()

    cursor = conector.cursor()

    comando = f'select * from convidados where id={n_convidado};'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    cursor.close()
    conector.close()

    return resultado[0]


def head_reorganizaOrdem():
    conector = head_conector()

    cursor = conector.cursor()

    comando = f'SET @num := 0;'
    cursor.execute(comando)
    conector.commit()
    comando = f'UPDATE convidados SET id = @num := (@num+1);'
    cursor.execute(comando)
    conector.commit()
    comando = f'ALTER TABLE convidados AUTO_INCREMENT =1;'
    cursor.execute(comando)
    conector.commit()


    cursor.close()
    conector.close()


def head_excluirConvidado(id):
    try:
        conector = head_conector()
    except:
        print('Erro ao conectar com o banco de dados do "db_convidados" do MySQL')
    else:
        try:    
            cursor = conector.cursor()
            comando = f'delete from convidados where id={id};'
            cursor.execute(comando)
            conector.commit()
        except:
            print('Erro ao tentar fazer a exclusão desses dados em "db_convidados" do MySQL')
        else:
            print('-'*37)
            print(f'Convidado removido com sucesso.')
            print('-'*37)
            cursor.close()
            conector.close()


def head_alterarCadastro(opt, nConv, nome, idade):
    try:    #tentativa de acessar banco de dados do MySQL
        conector = head_conector()
    except:
        print('Erro ao conectar com o banco de dados "db_convidados" do MySQL')
    else:
        try:    #tentativa de fazer uma inserção de dados no MySQL
            cursor = conector.cursor()
            if opt==1:
                cud = f'update convidados set nome="{nome}" where id={nConv}'
            elif opt==2:
                cud = f'update convidados set idade={idade} where id={nConv}'
            elif opt==3:
                cud = f'update convidados set nome="{nome}", idade={idade} where id={nConv}'
            cursor.execute(cud)
            conector.commit()
        except:
            print('Erro ao tentar fazer a inserção desses dados em "db_convidados" do MySQL')
        else:
            print('-'*37)
            print(f'Alteração feita com sucesso.')
            print('-'*37)
            cursor.close()
            conector.close()

