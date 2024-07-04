num1 = int(input('Digite o início da contagem: '))
num2 = int(input('Digite o final da contagem: '))
option = str(input('Mostrar contagem em pares ou ímpares: ')).strip()
lista = []

if option.lower() in ('par', 'pares'):
    for a in range(num1, num2+1):
        if a%2==0:
            lista.append(int(a))
    print(lista)

elif option.lower() in ('ímpares', 'impares', 'ímpar', 'impar'):
    for a in range(num1, num2+1):
        if a%2==1:
            lista.append(int(a))
    print(lista)

else:
    print(f'[ERRO] Você digitou "{option}", reinicie o teste e escolhe entre pares ou ímpares!')

