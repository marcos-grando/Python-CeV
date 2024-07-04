#IMC = peso/(altura²)
peso = float(input('Seu peso em kg: '))
altura = float(input('Sua altura em m: '))
imc = float(peso/(altura**2))
print(imc)

if imc<18.5:
    print('Abaixo do peso!')
elif 18.5<=imc<25: 
    print('Peso ideal!')
elif 25<=imc<30:
    print('Sobrepeso!')
elif 30<=imc<40:
    print('Obesidade!')
elif imc>=40:
    print('Obesidade mórmida!')