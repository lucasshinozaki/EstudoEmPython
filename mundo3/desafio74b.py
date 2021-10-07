#Desafio 74
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e também indique o menor e o mais valor que estão na tupla
from random import randint
numeros = tuple(randint(1, 10) for i in range(0, 5))

print("Os valores sorteados foram: ", end="")
for n in numeros:
    print(f'{n} ', end="")

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')