
text = str(input('Digite o texto: ')).strip()
text1 = text[::-1]

if text.lower()==text1.lower():
    print(f'É Palíndromo!')
    print(f'Normal: "{text}"')
    print(f'Invertido: "{text1}"')
elif text.lower()!=text1.lower():
    print('Não é Palíndromo!')
    print(f'Normal: "{text}"')
    print(f'Invertido: "{text1}"')    

    ''' versão guanabara
frase = str(input('Digite a frase ou palavra: )).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

    '''

