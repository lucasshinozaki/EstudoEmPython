# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher.
# Só que agora utilizando um laço for

n = int(input('Digite um numero: '))

for c in range(0, 11):
    print('{} * {} = {}'.format(n, c, n * c))
