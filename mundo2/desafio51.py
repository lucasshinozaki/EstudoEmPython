#Desenvolva um programa que leia o primeiro termo e a razão de uma PA
#No final, mostre os 10 primeiro termos dessa progressão

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
i = 0

for c in range(primeiro_termo, (primeiro_termo + (10 - 1) * razao) + 1, razao):
    i += 1
    print('{} : {}'.format(i, c))

#i =0
#lista = []
#for c in range(2, 50, 2):
#    i += 1
#    lista.insert(i, c)

#for cont in range(len(lista)):
#    if cont <= 10:
#        print("{} = {}".format(cont, lista[cont]))

