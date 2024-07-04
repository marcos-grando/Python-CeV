def fatorial(número, mostrar=False):
    """
    ->Cálculo fatorial de um número
    :param número: Número desejado para fatorar;
    :param mostrar(opcional): [True]=Mostrar cálculo, [False]=Apenas resultado;
    :return: Retorna 'número' fatorado; com ou sem cálculo fatorial.
    """
    número_fatorado = 1
    if mostrar==False:
        for fatorial in range(número, 0, -1):
            número_fatorado *= fatorial
    if mostrar==True:
        for fatorial in range(número, 0, -1):
            número_fatorado *= fatorial
            print(f'{fatorial}', end=' ')
            print('x'if fatorial>1 else'=', end=' ')
    return número_fatorado

print('=-'*15)
print(fatorial(5, True))
print('=-'*15)
help(fatorial)
