from mydefs_package.mycores_mdl.mycores import *
from mydefs_package.defsGood_mdl.defsGood import * 
from mydefs_package.formatime_mdl.formatime import head_timeTitle
from mydefs_package.lerNumber_mdl.defs_readn import readn_cleanNum
from locale import LC_MONETARY, currency, setlocale
setlocale(LC_MONETARY, 'pt_BR.UTF-8')
from random import randint
from time import sleep

def traço_vertical(mensagem, speed=0.05, espaço_esq=0, espaço_dir=0):
    print(bold_('|'+' '*espaço_esq, 8), end='')
    head_timeTitle(mensagem, False, speed)
    print(bold_(' '*espaço_dir+'|', 8))

moneyBase = 100       # a base de cálculo da premiação  
recompensasReal = []  # número formatado por preço lc_monetary
recompensasNumb = []  # número real sem formatação
sorteioTotal = 6      # necessário ser 6; toda formatação foi feita nessa base

while True:
    head_timeTitle(bold_('+', 8)+bold_('-'*9, 4)+bold_('[ MEGA inSANA! ]', 8)+bold_('-'*9, 4)+bold_('+', 8), True, 0.02)
    traço_vertical(f'{f'{neutro_(' Sorteamos ', 8)+bold_(f'{sorteioTotal} números ', 6)+neutro_('diferentes', 8)}':^60}', 0.02)
    traço_vertical(f'{f'{neutro_(' Você terá ', 8)+bold_(f'{sorteioTotal} chances ', 6)+neutro_('de acertar', 8)}':^60}', 0.02)
    traço_vertical(f'{f'{neutro_('   Números sorteados ', 8)+bold_('entre 1~60', 6)}':<52}', 0.02)

    for premiação in range(sorteioTotal):   # cálculo dos prêmios
        recompensasReal.append(currency(moneyBase, True, True))
        recompensasNumb.append(moneyBase)
        if moneyBase<=1000000:
            moneyBase*=10
        else:
            moneyBase*=2

    traço_vertical(f'{f'{bold_('-'*(len(recompensasReal[0])+9), 4)}':<42}', 0.01, 2)
    traço_vertical(bold_('Nossos prêmios', 8), 0.07, 4, 16)
    traço_vertical(f'{f'{bold_('-'*(len(recompensasReal[0])+9), 4)}':<42}', 0.01, 2)

    for pontos, premio in enumerate(recompensasReal[:-1]):  # amostragem dos prêmios já calculado
        if pontos==0:
            traço_vertical(f'{f'{bold_(f'{pontos+1} pt:', 8)}  {bold_(recompensasReal[pontos], 6)}':<46}', 0.02, 2, 6)
        else:
            traço_vertical(f'{f'{bold_(f'{pontos+1} pts:', 8)} {bold_(recompensasReal[pontos], 6)}':<46}', 0.02, 2, 6)

    traço_vertical(bold_(f'{f'{'-'*29}':<32}', 4), 0.01, 2)
    traço_vertical(f'{f'{neutro_('ACEERTOU TUDO?', 8)}':^42}')
    traço_vertical(f'{f'{bold_(f'>>> {recompensasReal[-1]} <<<', 6)}':^44}')
    traço_vertical(bold_('=', 8)+bold_('-'*32, 4)+bold_('=', 8), 0.01)

    meusBilhetes = []   # números escolhidos nos bilhetes
    sorteio = []        # os 6 números sorteados
    for sorteioNum in range(sorteioTotal):
        sorteio.append(randint(1,60))
    print('     ', sorteio)
    bilheteMax = 3

    while True:
        head_timeTitle(neutro_('    Você recebeu ', 8)+bold_('três bilhetes!!', 6), True, 0.02)
        head_timeTitle(neutro_('  Quer apostar quantos ', 8)+bold_('bilhetes', 6)+bold_('?', 8), False, 0.02)
        bilhetes = input(f' {cor_bold(6)}').strip().lower()
        cor_bold()
        while bilhetes not in('0', '1', '2', '3'):
            head_timeTitle(neutro_('Você têm somente ', 8)+bold_('3 bilhetes', 6))
            head_timeTitle(neutro_('Quanto quer ', 8)+bold_('apostar', 6)+bold_('?', 8), False, 0.02)
            bilhetes = input(f' {cor_bold(6)}').strip().lower()
            cor_bold()
        bilhetes = int(bilhetes)
        traço_vertical(bold_('=', 8)+bold_('-'*32, 4)+bold_('=', 8), 0.02)

        if bilhetes==0:
            fim=True
            break
        else:
            acabou=False
            usarTodos=False
            bilheteUsado=0
            while True:
                bilheteUsado+=1
                meusBilhetes.append([])
                print(' '*5, end='')
                arrasta_pLadoTxt(f'[ {bilheteUsado}º bilhete ]', True, 8, 4, 4, 1, 0.035)
                print(' '*11, end='')
                head_timeTitle(bold_('-'*14, 4), True, 0.02)
                for apostas in range(sorteioTotal):     # solicita os números para os bilhetes 
                    print(' '*12, end='')
                    head_timeTitle(neutro_(f'{f'{apostas+1}º número:'}', 8), False)
                    apostaNum = input(f' {cor_bold(6)}').strip().lower()
                    cor_bold()
                    while apostaNum.isnumeric()==False:
                        print(' '*5, end='')
                        head_timeTitle(neutro_(f'{f'[ERRO] Tente novamente'}', 3), True)
                        print(' '*12, end='')
                        head_timeTitle(neutro_(f'{f'{apostas+1}º número:'}', 8), False)
                        apostaNum = input(f' {cor_bold(6)}').strip().lower()
                        cor_bold()
                    apostaNum = int(apostaNum)
                    meusBilhetes[bilheteUsado-1].append(apostaNum)
                    print(' '*11, end='')
                    head_timeTitle(bold_('-'*14, 4), True, 0.02)
                if bilheteUsado==bilheteMax:
                    acabou = True
                    fim=True
                    break
                elif bilheteUsado>=bilhetes and usarTodos==False: #pergunta se deseja usar os bilhetes que sobraram
                    traço_vertical(bold_('=', 8)+bold_('-'*32, 4)+bold_('=', 8), 0.02)
                    if (bilheteMax-bilheteUsado)==1:      
                        head_timeTitle(' '*5+bold_('Ainda lhe resta ', 8)+bold_('1 bilhete', 6)+bold_('!',8), True, 0.02)
                        head_timeTitle(' '*7+bold_('[',8)+bold_('1',6)+bold_('] Usar', 8)+' '*6+bold_('[',8)+bold_('2',6)+bold_('] Sair', 8)+' '*7, True, 0.02)
                        head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
                        pergunta = input(f' {cor_bold(6)}').strip().lower()
                        cor_bold()
                        while pergunta not in('1', '2'):
                            head_timeTitle(bold_('[', 8)+bold_('ERRO', 1)+bold_(']', 8)+neutro_('Opção inválida!',8))
                            head_timeTitle(neutro_('Você têm somente ', 8)+bold_('1 bilhete', 6))
                            head_timeTitle(' '*7+bold_('[',8)+bold_('1',6)+bold_('] Usar', 8)+' '*6+bold_('[',8)+bold_('2',6)+bold_('] Sair', 8)+' '*7, True, 0.02)
                            head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
                            pergunta = input(f' {cor_bold(6)}').strip().lower()
                            cor_bold()
                        pergunta = int(pergunta)
                        if pergunta==1:
                            continue
                        elif pergunta==2:
                            fim=True
                            break
                    else:
                        head_timeTitle(' '*4+bold_('Lhe restam ', 8)+bold_(f'{bilheteMax-bilheteUsado} bilhetes', 6)+bold_('! Usar?', 8), True, 0.02)
                        head_timeTitle(' '*2+bold_('[',8)+bold_('1',6)+bold_('] Só um', 8)+' '*3+bold_('[',8)+bold_('2',6)+bold_('] Todos', 8)+' '*3+bold_('[',8)+bold_('3',6)+bold_('] Sair', 8)+' '*2, True,0.02)
                        head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
                        pergunta = input(f' {cor_bold(6)}').strip().lower()
                        cor_bold()
                        while pergunta not in('1', '2', '3'):
                            head_timeTitle(bold_('[', 8)+bold_('ERRO', 1)+bold_(']', 8)+neutro_('Opção inválida!',8))
                            head_timeTitle(neutro_('Você têm ao todo', 8)+bold_(f'{bilheteMax-bilheteUsado} bilhetes'+bold_('! Usar?', 8), 6))
                            head_timeTitle(' '*2+bold_('[',8)+bold_('1',6)+bold_('] Só um', 8)+' '*3+bold_('[',8)+bold_('2',6)+bold_('] Todos', 8)+' '*3+bold_('[',8)+bold_('3',6)+bold_('] Sair', 8)+' '*2, True,0.02)
                            head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
                            pergunta = input(f' {cor_bold(6)}').strip().lower()
                            cor_bold()
                        pergunta = int(pergunta)
                        if pergunta==1:
                            continue
                        elif pergunta==2:
                            usarTodos = True
                            continue
                        elif pergunta==3:
                            fim=True
                            break
        if fim==True:
            break

    meusAcertos = []    # número de acertos por bilhete
    for apostas in meusBilhetes:
        pts=0
        for acerto in apostas:
            if acerto in sorteio:
                pts+=1
        meusAcertos.append(pts)

    traço_vertical(bold_('=', 8)+bold_('-'*32, 4)+bold_('=', 8), 0.02)
    if acabou==True:
        head_timeTitle(' '*2+bold_('Que pena!', 6)+bold_(' Seus bilhetes acabaram', 8), True, 0.02)
        head_timeTitle(' '*4+bold_('Sortearemos neste momento...', 8), True, 0.04)
    else:
        if (bilheteMax-bilheteUsado)==1:
            head_timeTitle(' '*2+bold_('Que pena! Desperdiçou ', 8)+bold_(f'{bilheteMax-bilheteUsado} bilhete', 6), True, 0.03)
        elif (bilheteMax-bilheteUsado)>1:
            head_timeTitle(' '*2+bold_('Que pena! Desperdiçou ', 8)+bold_(f'{bilheteMax-bilheteUsado} bilhetes', 6), True, 0.03)
        head_timeTitle(' '*5+bold_('Então sortearemos agora...', 8), True, 0.04)
    head_timeTitle(' '*5+bold_('Os NÚMEROS', 6)+bold_(' da MEGA inSANA', 8))
    print('')

    head_timeTitle(bold_('+', 8)+bold_('-'*5, 4)+bold_('[ Sorteio MEGA inSANA! ]', 8)+bold_('-'*5, 4)+bold_('+', 8), True, 0.01)
    traço_vertical(' '*2+bold_('-'*30, 4)+' '*2, 0.01)

    print(bold_('|', 8)+' '*2, end='')
    for numSorteio in sorteio:      # amostragem do sorteio
        if numSorteio<10:
            if numSorteio==sorteio[-1]:
                head_timeTitle(' '*1+bold_(f'0{numSorteio}', 8)+' '*4+bold_('|', 8), True, 0.025)
            else:
                head_timeTitle(' '*1+bold_(f'0{numSorteio}', 8)+' '*1+bold_('|', 8), False, 0.025)
        else:
            if numSorteio==sorteio[-1]:
                head_timeTitle(' '*1+bold_(numSorteio, 8)+' '*4+bold_('|', 8), True, 0.025)
            else:
                head_timeTitle(' '*1+bold_(numSorteio, 8)+' '*1+bold_('|', 8), False, 0.025)
    
    traço_vertical(' '*2+bold_('-'*30, 4)+' '*2, 0.01)

    traço_vertical(bold_('Seus bilhetes', 8), 0.07, 10, 11)
    traço_vertical(f'{f'{bold_('-'*(len('Seus bilhetes')+2), 4)}'}', 0.025, 9, 10)


    for n, bilheteTotal in enumerate(meusBilhetes):       # amostragem dos bilhetes (com número em verde se for um acerto)
        traço_vertical(neutro_(f'{n+1}º bilhete', 8)+(bold_(f' ({meusAcertos[n]}pt) ', 8) if meusAcertos[n]<2 else bold_(f' ({meusAcertos[n]}pts)', 8)), 0.03, 8, 9)
        print(bold_('|', 8)+' '*2, end='')
        for n, bilheteNum in enumerate(bilheteTotal):
            if bilheteNum<10:
                if n+1==len(bilheteTotal):
                    head_timeTitle(' '*1+f'{bold_(f'0{bilheteNum}', 8) if bilheteNum not in sorteio else bold_(f'0{bilheteNum}', 2)}'+' '*4+bold_('|', 8), True, 0.025)
                else:
                    head_timeTitle(' '*1+f'{bold_(f'0{bilheteNum}', 8) if bilheteNum not in sorteio else bold_(f'0{bilheteNum}', 2)}'+' '*1+bold_('|', 8), False, 0.025)
            else:
                if n+1==len(bilheteTotal):
                    head_timeTitle(' '*1+f'{bold_(bilheteNum, 8) if bilheteNum not in sorteio else bold_(f'{bilheteNum}', 2)}'+' '*4+bold_('|', 8), True, 0.025)
                else:
                    head_timeTitle(' '*1+f'{bold_(bilheteNum, 8) if bilheteNum not in sorteio else bold_(f'{bilheteNum}', 2)}'+' '*1+bold_('|', 8), False, 0.025)
        traço_vertical(f'{f'{bold_(' '*(len('0º bilhete')+2), 4)}':<42}', 0.01, 2)
    
    traço_vertical(' '*2+bold_('-'*30, 4)+' '*2, 0.01)
    traço_vertical(bold_('Ganhos/prêmios', 8), 0.02,10,10)
    traço_vertical(' '*2+bold_('-'*30, 4)+' '*2, 0.01)

    prêmiosGanhos = []

    for n, premiando in enumerate(meusBilhetes): #amostragem final dos bilhetes e seus ganhos
        if meusAcertos[n]==0:
            traço_vertical(f'{f'{neutro_(f'{n+1}º bilhete: ', 8)+bold_('R$ 0,00 ', 6)}':<48}', 0.03, 3, 1)
            prêmiosGanhos.append(0)
        else:
            traço_vertical(f'{f'{neutro_(f'{n+1}º bilhete: ', 8)+bold_((recompensasReal[meusAcertos[n]-1]), 6)}':<48}', 0.03, 3, 1)
            prêmiosGanhos.append(recompensasNumb[meusAcertos[n]-1])

    traço_vertical(' '*2+bold_('-'*30, 4)+' '*2, 0.01)

    for n, soma in enumerate(prêmiosGanhos):  # cálculo do total somado entre os ganhos
        if n==0:
            total=soma
        else:
            total+=soma
    total = currency(total, True, True)

    if total==0:
        traço_vertical(neutro_('Vcoê ganhou R$ 0,00 ...'), 0.03, 3, 18)
        traço_vertical(neutro_('Boa sorte na próxima vez!!'), 0.03, 3, 18)    
    else:
        traço_vertical(f'{f'{neutro_('Você ganhou ', 8)+bold_(f'{total}', 6)}':<49}', 0.04, 3)
    traço_vertical(bold_('=', 8)+bold_('-'*32, 4)+bold_('=', 8), 0.01)

    
    head_timeTitle(' '*4+neutro_('Deseja ', 8)+bold_('iniciar ', 6)+neutro_('um ', 8)+bold_('novo jogo', 6)+neutro_('?', 8),True,0.02)
    head_timeTitle(' '*2+bold_('[',8)+bold_('1',6)+bold_('] Novo jogo', 8)+' '*3+bold_('[',8)+bold_('2',6)+bold_('] Sair do jogo', 8)+' '*2,True,0.02)
    head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
    pergunta = input(f' {cor_bold(6)}').strip().lower()
    cor_bold()
    while pergunta not in('1', '2'):
        head_timeTitle(bold_('[', 8)+bold_('ERRO', 1)+bold_(']', 8)+neutro_('Opção inválida!',8))
        head_timeTitle(' '*4+neutro_('Deseja ', 8)+bold_('iniciar ', 6)+neutro_('um ', 8)+bold_('novo jogo', 6)+neutro_('?', 8),True,0.02)
        head_timeTitle(' '*2+bold_('[',8)+bold_('1',6)+bold_('] Novo jogo', 8)+' '*3+bold_('[',8)+bold_('2',6)+bold_('] Sair do jogo', 8)+' '*2,True,0.02)
        head_timeTitle(' '*4+bold_('Seu ', 8)+bold_('Desejo',6)+bold_(':',8), False, 0.01)
        pergunta = input(f' {cor_bold(6)}').strip().lower()
        cor_bold()
    pergunta = int(pergunta)
    if pergunta==1:
        continue
    elif pergunta==2:
        break



head_timeTitle(bold_('+', 8)+bold_('-'*4, 4)+'[ Encerrando MEGA inSANA ]'+bold_('-'*4, 4)+bold_('+', 8), True, 0.03)
traço_vertical(' '*4+bold_('-'*26, 4)+' '*4, 0.025)
traço_vertical(bold_('VOLTE SEMPRE', 6), 0.06, 11, 11, 0.025)
traço_vertical(' '*4+bold_('-'*26, 4)+' '*4, 0.025)
head_timeTitle(bold_('+', 8)+bold_('-'*4, 4)+'[ MEGA inSANA encerrada! ]'+bold_('-'*4, 4)+bold_('+', 8), True, 0.03)
 
          