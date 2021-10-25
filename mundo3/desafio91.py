#Desafio 91
#Crie um programa onde 4 jogadores um dado e tenham resultados aleatórios
#Guarde esses resultados em um dicionário
#No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado
lista = list()
from random import randint
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print("Valores sorteados: ")

for k, v in jogo.items():
    print(f'        O {k} tirou {v}')

print("Ranking dos jogadores:")
lista.append(sorted(jogo.values(), reverse=True))

cont = cont1 = cont2 = cont3 = cont4 = 0
for v in lista:
    for j in v:
        cont += 1
        print(f"        {cont} lugar:", end=" ")
        if jogo['jogador1'] == j and cont1 == 0:
            print('jogador1', end=" ")
            cont1 += 1
        elif jogo['jogador2'] == j and cont2 == 0:
            print('jogador2', end=" ")
            cont2 += 1
        elif jogo['jogador3'] == j and cont3 == 0:
            print('jogador3', end=" ")
            cont3 += 1
        elif jogo['jogador4'] == j and cont4 == 0:
            print('jogador4', end=" ")
            cont4 += 1
        print(f'com {j}')
