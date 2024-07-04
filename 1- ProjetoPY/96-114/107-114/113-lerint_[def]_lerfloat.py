from mydefs_package.lernumber_mdl.defs_readn import readn_lerfloat, readn_lerint

print(readn_lerint('Digite um valor inteiro: '))        #para testar:  46abc ; 4,5 ; 4.5 ; , ; .7 ; 4- ; 4+ ; 4-+ ; -+8 ; +-8

print('='*57)

print(readn_lerfloat('Digite um valor decimal: '))      #para testar:  46abc ; 4,,5 ; 4..8 ; .- ; ,-4 ; 4- ; 4+ ; +-5 ; -+5 ; 6-+

#print(lerfloat('Valor númerico: ')) # 46abc ; 4,,5 ; 4..8 ; 5,.7 ; ,-4 ; 4-7 ; 4+6 ; 46+ ; 47- ; 6-+ ; +-5 ; -+5
#print(lerint('Valor númerico: ')) # 46aabc ; 4,5 ; 4.5 ; .7 ; ,8 ; 4- ; 4+ ; 4+7 ; 4-7 ; 4-+ ; -+8 ; +-8