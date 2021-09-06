import random

num = random.randint(0, 5)
num1 = int(input('Digite um numero entre 0 a 5: '))

if num == num1:
    print('PARABÉNS')
else:
    print('[ERROU], O numero era {}'.format(num))
