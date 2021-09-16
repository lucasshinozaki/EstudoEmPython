import random
nome1 = input('Digite o nome1: ')
nome2 = input('Digite o nome2: ')
nome3 = input('Digite o nome3: ')
nome4 = input('Digite o nome4: ')

lista = [nome1, nome2, nome3, nome4]
r = ['lucas', 'japa ama mais', 'asuna', 'lucas']

print(lista)

random.shuffle(r)
random.shuffle(lista)

print('Grupo 1: ', r)
print('Grupo 2: ', lista)

print('Ordem de apresentação do grupo1:')
print('\n'.join('{}: {}'.format(*k) for k in enumerate(r)))

print('Ordem de apresentação do grupo2:')
print('\n'.join('{}: {}'.format(*k) for k in enumerate(lista)))

