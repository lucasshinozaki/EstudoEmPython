#Desafio 74
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e também indique o menor e o mais valor que estão na tupla
import random
tupla = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
tupla2 = tuple(random.randint(1, 10) for i in range(0, 5))
print(tupla2)
maior = menor = 0
for c in range(0, 5):
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        elif tupla[c] < menor:
            menor = tupla[c]

print(f"Os valores sorteados foram: {tupla}")
print(f"O maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")
