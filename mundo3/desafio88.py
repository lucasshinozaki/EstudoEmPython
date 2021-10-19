#Desafio 88
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60
#Para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

listaComposta = list()
listaAleatoria = list()
qtdDeJogo = int(input("Quantos jogos você quer que eu sortei? "))

for linha in range(0, qtdDeJogo):
    for coluna in range(0, 6):
        valor = randint(1, 60)
        if valor not in listaAleatoria:
            listaAleatoria.append(valor)
        else:
            while valor in listaAleatoria:
                valor = randint(1, 60)
            listaAleatoria.append(valor)
    listaAleatoria.sort()
    listaComposta.append(listaAleatoria[:])
    listaAleatoria.clear()

print("-="*30)
for c in range(0, qtdDeJogo):
    print(f"Jogo {c + 1}: {listaComposta[c]}")
print("-="*30)
