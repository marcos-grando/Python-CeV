def voto(ano_atual, user_nascimento):
    user_idade = ano_atual - user_nascimento
    if user_idade<16:
        print('Voto negado!')
    elif user_idade==16 or user_idade==17:
        print('Voto opcional.')
    elif user_idade>=18:
        print('Voto obrigatório!')

anoAtual = 2024
while True:
    userNasc = int(input('Ano de nascimento: '))
    if userNasc==0:
        break
    voto(anoAtual, userNasc)
    print('=-'*12)