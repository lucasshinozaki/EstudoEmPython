# Desafio 98
# Faça um programa que tenha uma função chamada contador(). que receba três parâmetros: inicio, fim e passo e realiza a contagem
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if passo == 0:
        passo = 1
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
    else:
        if passo > 0:
            passo = passo * -1
        for c in range(inicio, fim - 1, passo):
            print(c, end=" ")

    print("FIM!")
    print("--" * 20)


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("--" * 20)

contador(inicio, fim, passo)