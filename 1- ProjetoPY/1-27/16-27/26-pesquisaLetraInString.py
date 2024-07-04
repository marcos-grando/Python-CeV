frase = str(input('Digite uma frase: ')).strip()
print(f'Usando X vemos a letra A repetindo {frase.upper().count('A')} vezes')
print(f'Usando X vemos que a letra A aparece em {frase.upper().find('A')+1} pela primeira vez')
print(f'Usando X vemos que a letra A aparece em {frase.upper().rfind('A')+1} pela última vez')


