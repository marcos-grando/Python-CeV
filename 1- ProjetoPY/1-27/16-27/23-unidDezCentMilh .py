num = int(input('Digite um número: '))
unid = num  // 1 % 10 
deze = num  // 10 % 10
cent = num  // 100 % 10
milh = num  // 1000 % 10
print(f'Analisando {num}!')
print(f'Unidade: {unid} \nDezena: {deze} \nCentena: {cent} \nMilhar: {milh}!')

#O mesmo exercício pode ser feito com 'if' ou utilizando num1 = srt(num) ---> {num1[0,1,2,3]}
'''
A idéia aqui é citar o número que corresponde o início de cada sistema
númerico: unidade, dezena, centena e milhar. Nesse caso aqui, utilizamos
a divisão de 1/10/100/1000 (correspondendo cada sistema) e depois disso
com o valor do resto da divisão por 10 (% 10). 
Exemplo: (divisão inteira:) 1234//10 = 123 --> 123/10 = 12,3 ---> 1234//10%10 = 2
(nesse exemplo a última unidade antes da vírgula foi 2, esse é o resto)
'''





