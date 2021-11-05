#Desafio 100
#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar()
#A primeira função vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos
#os pares sorteados pela função anterior
from random import randint

lista = list()

def sorteia():
    print("Sorteando 5 valores pares: ", end="")
    for c in range(0, 5):
        num = randint(0, 9)
        print(num, end=" ")
        lista.append(num)
    print("PRONTO!")


def somaPar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de {lista}, temos {soma}")


sorteia()
somaPar()
