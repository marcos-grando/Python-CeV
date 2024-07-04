lDict = []
c=f=0
while True:
    print('--'*7)
    lDict.append({})
    aluno = str(input('Aluno: ')).title().strip()
    if aluno.lower()=='stop':
        del lDict[-1]
        break
    if len(aluno)>f:
        f=(len(aluno))
    
    lDict[c]["Nome"] = aluno
    lDict[c]["Nota1"] = float(input('1º nota: '))
    if lDict[c]["Nota1"]>10:
        lDict[c]["Nota1"] = float(input('[ERRO] Digite nova válida:'))
    
    lDict[c]["Nota2"] = float(input('2º nota: '))
    if lDict[c]["Nota2"]>10:
        lDict[c]["Nota2"] = float(input('[ERRO] Digite nova válida:'))
    
    lDict[c]["Média"] = (lDict[c]["Nota1"]+lDict[c]["Nota2"])/2
    if lDict[c]["Média"]>=7.0:
        lDict[c]["Status"]='Aprovado'
    elif lDict[c]["Média"]<7.0:
        lDict[c]["Status"]='Reprovado'
    
    c+=1

print('')    
print('='*(10+10+7+f))
esp = 9
espN = f+3
print(f'{'Nome':<{espN}} | {'Média':^{esp}} | {'Status':>{esp}}')
for p in lDict:
    print(f'{p["Nome"]:<{espN}} | {p["Média"]:^{esp}} | {p["Status"]:>{esp}}')
print('='*(10+10+7+f))
print('')


