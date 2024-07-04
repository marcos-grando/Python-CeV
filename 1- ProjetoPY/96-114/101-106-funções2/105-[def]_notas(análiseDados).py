def notas(* notas_alunos, status=False):
    """
    -> Recebe quantidade indeterminada de notas. Executa esses dados fazendo análise 
    e retornando informações/detalhes sobre as notas.
    -> Entre os dados têm: Total de notas informadas; Maior nota informada; Menor nota informada; 
    Média das notas informadas; E, se optado, o status da média dessas notas.
    :param notas_alunos: Recebe todas as notas que o usuário tiver;
    :param status: [True] recebe a situação da média das notas;
    """
    maior_nota=menor_nota=quantidade=soma=0
    for nota in notas_alunos:
        if nota>maior_nota:
            maior_nota=nota
        if nota<menor_nota or quantidade==0:
            menor_nota=nota
        soma+=nota
        quantidade+=1
    média = soma/quantidade
    if status==False:
        dados_notas = {"Nº de notas": quantidade, "Maior nota": maior_nota, "Menor nota": menor_nota, "Média": média}
    elif status==True:
        dados_notas = {"Nº de notas": quantidade, "Maior nota": f'{maior_nota:.2f}', "Menor nota": f'{menor_nota:.2f}', "Média": f'{média:.2f}'}
        if média<5: dados_notas["Status"]='Horroroso'
        elif 7>média>=5: dados_notas["Status"]='Razoável'
        elif 9>média>=7: dados_notas["Status"]='Na média'
        elif média>=9: dados_notas["Status"]='Excelente'
    return dados_notas

print(notas(8,9,10,9,8,9,10,10, status=True))