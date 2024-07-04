def txtTitle(txtTitle):
    print('-'*(len(txtTitle)+6))
    print(f'{f'{txtTitle}':^{len(txtTitle)+6}}')
    print('-'*(len(txtTitle)+6))

while True:
    txt = input('Título: ').upper()
    if txt.lower()=='stop':
        break
    txtTitle(txt)
txtTitle('Programa Encerrado')