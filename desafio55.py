#Desafio 55
#Faça um programa que leia o peso de cinco pessoas
#No final, mostre qual foi o maior e menor peso lidos

maior = 0
menor = 1000

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if(peso > maior):
        maior = peso
    elif(menor < peso):
        menor = peso

print("O maior peso: {}".format(maior))
print("O menor peso: {}".format(menor))
