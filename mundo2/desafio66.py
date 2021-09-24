#Desafio 66
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar.
#o ovalor 999, que é a condição de parada. No final, mostre quantos números forma digitados e qual foi a soma entre eles
#(desconsiderando o flag)
cont = soma = 0
while True:
    numero = int(input("Digite um valor (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f"A soma dos {cont} valores foi {soma}!")
