#Desafio 71
#Crie um programa que simule o funcionamento de um caixa eletrônico
#no inicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
#E o programa vai informar quantas cédulas de cada valor serão entregues
#OBS: Considere que o caixa possui R$50, R$20m R$10 e R$1

while True:
    valor = int(input("Que valor você quer sacar ? R$"))
    cedula50 = valor // 50
    valor -= cedula50 * 50
    cedula20 = valor // 20
    valor -= cedula20 * 20
    cedula10 = valor // 10
    valor -= cedula10 * 10
    cedula1 = valor // 1
    valor -= cedula1 * 1
    if valor == 0:
        break
print(f"Total de {cedula50} cédulas de R$50")
print(f"Total de {cedula20} cédulas de R$20")
print(f"Total de {cedula10} cédulas de R$10")
print(f"Total de {cedula1} cédulas de R$1")