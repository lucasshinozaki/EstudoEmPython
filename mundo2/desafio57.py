#Desafio 57
#Faça um programa que leia o sexo de uma pessoa
#Mas só aceite os valores 'M' ou 'F'.
#Caso esteja erradp, peça a digitação novamente até te um valor correto.

sexo = input('Digite o seu sexo [F/M]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Entrada inválida! Digite novamente o seu sexo [F/M]: ').strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
