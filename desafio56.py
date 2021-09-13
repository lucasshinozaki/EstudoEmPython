#Desafio56
#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
#No final do programa, mostre?
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

soma = 0
cont = 0
maior = 0

for c in range(0, 3):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo {M:Masculino, F:Feminino}: "))

    soma += idade
    if(idade > maior and sexo == "M"):
        maisvelho = nome
    if(idade < 20 and sexo == "F"):
        cont += 1


media = soma / 4
print("A media das idades: {:.2f}".format(media))
print("O nome do mais velho: {}".format(maisvelho))
print("Quantidade de mulheres menores de 20 anos: {}".format(cont))
