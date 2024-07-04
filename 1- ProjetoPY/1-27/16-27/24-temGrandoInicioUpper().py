city = str(input('Qual sua cidade natal? ')).strip()
print(city[:5].upper()=='SANTO')

'''
Aqui, por ter [:5], se refere a comparação no 
INÍCIO da frase usada no input. 

[:5] --> inicia no 0 e vai até o caracter 5;
'.strip()' --> retira espaços da frente e trás;
.upper() --> faz com que o valor escrito no input
seja colocado em letras maiúscula, ao mesmo tempo que
compara com o "=='SANTO'", dessa forma a comparação fica
entre duas palavras em maiúscula e sejam iguais. 

Poderia ser usado .lower() comparando com "=='santo'".
'''