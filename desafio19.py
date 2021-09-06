import random
nome1 = input("Digite um nome1 : ")
nome2 = input("Digite um nome2 : ")
nome3 = input("Digite um nome3 : ")
nome4 = input("Digite um nome4 : ")
lista = [nome1, nome2, nome3, nome4]
r = random.choice(['lucas', 'japa ama mais', 'asuna', 'lucas'])
r1 = random.choice(lista)
print('O escolhido foi: {}, {}'.format(r, r1))

