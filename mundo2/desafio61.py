#Desafio 61
#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
#mostrando os 10 primeiro termos da progressão usando a estrutura while

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

cont = 0
pa = 0
while cont != 10:
    print('{} : {}'.format(cont, primeiro_termo))
    primeiro_termo += razao
    cont += 1
