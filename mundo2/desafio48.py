#Desafio 48
#faça um programa que calcule a soma entre todos os números impares
#Que são muúltiplos de tre
#E que se encontram no intervalo de 1 até 500

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       soma += c

print('Soma eh {}'.format(soma))
