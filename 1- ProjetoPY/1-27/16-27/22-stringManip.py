nome = str(input('Nome completo: ')).title().strip()
print(f'Digitado: {nome}!')
print(f'Usando .upper() --> {nome.upper()}')
print(f'Usando .lower() --> {nome.lower()}')
print(f"Usando .len()-count(' ') --> Seu nome tem {len(nome)-nome.count(' ')} caracteres")

nomeSeparado = nome.split() #Separa as palavras da frase, criando uma lista com elas;
#print(nomeSeparado) -----> #Se necessário ver as palavras separadas;
print(f'Seu primeiro nome {nomeSeparado[0]} tem {len(nomeSeparado[0])} caracteres!')


