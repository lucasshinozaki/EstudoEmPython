# Desafio 93
# Crie um programa que gerencia o aproveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidadas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o capeonato.

jogador = dict()
lista_gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

soma = 0
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    soma += gols
    lista_gols.append(gols)

jogador['gols'] = lista_gols
jogador['total'] = soma
print("=-" * 30)
print(jogador)
print("=-" * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print("=-" * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
cont = 0
for k in jogador['gols']:
    print(f'    => Na partida {cont}, fez {k} gols.')
    cont += 1
print(f"Foi um total de {jogador['total']} gols.")