#Desafio 64
#Crie um programa que leia vários números inteiros pelo teclado
#O programa só vai parar quando o usuário digitar o valor 999
#O que é a condição de parada
#No final mostre quantos números forma digitados e qual foi a soma entre eles
#Desconsiderando o flag

n = 0
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input("Digite um numero :"))

print("Quantidade de números digitados: {}".format(cont - 1))
print("Soma dos numeros digitados: {}".format(soma))