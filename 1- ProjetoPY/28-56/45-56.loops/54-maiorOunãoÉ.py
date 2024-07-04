from datetime import date
pessoas = int(input('Grupo tem quantas pessoas? '))
year = date.today().year
nomes = []
datas = []
idades = []
for a in range(0, pessoas):
    nomes.append(str(input('Nome: ')))
    datas.append(int(input('Nasc: ')))
    idades.append(year-datas[a])
  
for b in range(0, pessoas):
    if 64>=idades[b]>=18:
        print(f'{nomes[b]} tem {idades[b]} anos! Dimaiór! Pode entrar!')
    elif idades[b]<18:
        print(f'{nomes[b]} tem {idades[b]} anos! Dimenór! Proibido entrada!')
    else:
        print(f'{nomes[b]} tem {idades[b]} anos! Velhocaduco! Por conta da casa!')
