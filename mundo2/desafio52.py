#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Digite um numero: '))
v = 0
for c in range(1, n+1):
    if n % c == 0:
        v += 1
        print('{} \ {} = {} somou +1 em v: {}'.format(n, c, n%c, v))
if v == 2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é um número primo!'.format(n))