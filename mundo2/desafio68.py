# Desafio 68
# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

cont = 0
while True:
    print("-=" * 30)
    valor = int(input("Diga um valor: "))
    parOuImpar = input("Par ou Impar? [P/I]: ").strip().upper()[0]
    computador = random.randint(0, 10)

    if (valor + computador) % 2 == 0:
        print("*" * 60)
        print(f"Você jogou {valor} e o computador {computador}. Total de {valor + computador} DEU PAR")
        print("*" * 60)
        if parOuImpar == "P":
            print("Você VENCEU!")
            cont += 1
        else:
            print("Você PERDEU!")
            break
    else:
        print("*" * 60)
        print(f"Você jogou {valor} e o computador {computador}. Total de {valor + computador} DEU IMPAR")
        print("*" * 60)
        if parOuImpar == "I":
            print("Você VENCEU!")
            cont += 1
        else:
            print("Você PERDEU!")
            break
print("-" * 60)
print(f"GAME OVER!! Você venceu {cont} vezes.")
