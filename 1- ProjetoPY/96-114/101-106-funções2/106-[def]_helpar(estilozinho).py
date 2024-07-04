from time import sleep
def helpar(quest): #retorna help()<-comando principal com estilozinho
    print('~'*51)
    print(f'{f" Acessando manual do comando '{quest}' ":-^{51}}')
    sleep(2)
    print()
    help(quest)
    sleep(3)
    print(f'{f" Manual do comando '{quest}' finalizado ":-^{51}}')
    print('~'*51)
    sleep(1.5)

#cabeçalho
print('='*51)
sleep(0.5)
print(f'{f'<<>> Hello User <<>>':-^{51}}')
sleep(0.2)
print('='*51)
sleep(0.3)
print(f'{f'Uma frescurinha para seu help()':^{51}}')
sleep(0.5)
print('~'*51)
sleep(2)

#comando principal
while True:
    quest = input('O que deseja helpar? ')
    sleep(1)
    if quest.lower()=='fim':
        print('~'*51)
        sleep(0.05)       
        print(f'{f' Helpar Finalizado ':-^{51}}')
        sleep(0.05)
        print('~'*51)
        break
    helpar(quest)
