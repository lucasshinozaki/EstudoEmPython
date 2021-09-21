#desafio 65
#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

opcao, cont, soma, maior, menor = 0, 0, 0, 0, 0
while(opcao != 2):
    n = int(input("Digite um número :"))
    print('''Opções:
    [1] - Deseja continuar
    [2] - Deseja sair do programa ''')
    opcao = int(input("Digite uma opcao: "))
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n

print("Media entre os números: {}".format(soma/cont))
print("O maior {}\nO menor: {}".format(maior, menor))
