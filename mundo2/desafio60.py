#Desafio 60
#Faça um programa que leia um número qualquer e mostre o seu fatorial

n = int(input('Digite um número: '))

cont = n
calculo = 1
while cont != 0:
    calculo *= cont
    cont -= 1

print('Por while: ')
print('O fatorial de {} é igual a: {}'.format(n, calculo))

calculo2 = 1
for c in range(1, n+1):
    calculo2 *= c

print('Por for:')
print('O fatorial de {} é igual a: {}'.format(n, calculo2))


