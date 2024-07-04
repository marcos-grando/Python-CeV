name = str(input('Nome completo: ')).strip()
print(f'Seu nome tem Grando? {'grando' in name.lower()}')

'''
Diferente da anterior ('24-.py'), aqui temos o uso de
'grando' in name.lower()', ou seja:
    o script vai colocar toda a variável 'name' em 'lower()'
    e comparar se há 'grando' em algum lugar do 'name';
    Diferente do exercício anterior que comparava apenas no INÍCIO,
    aqui analisará qualquer lugar no nome digitado.

No mais, foi usado a mesma lógica do '.upper()' em '24-.py', 
nesse caso usando o '.lower()'
'''