#Melhore o Desafio 28
#Onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar
#Mostrando no final quantos palpites forma necessários para vencer.

import random

num = random.randint(0, 10)
print(num);

n = 11
cont = 0

while num != n:
    n = int(input('Digite um numero entre 0 a 10: '))
    cont += 1

print('Parabens voce venceu!!')
print('QUantidade de tentativas: {}'.format(cont))
