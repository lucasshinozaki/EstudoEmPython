#Desafio 82
#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie duas lista extras que vão conter apenas os valores pares e os valores inpares digitados, respectivamente
#Ao final, mostre o conteúdo das três listas geradas.

opcao = ""
valores = list()
valoresPares = list()
valoresImpares = list()
while opcao != "N":
    valores.append(int(input('Digite um número: ')))
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()

for valor in valores:
    if valor % 2 == 0:
        valoresPares.append(valor)
    else:
        valoresImpares.append(valor)

print(f"A lista completa é {valores}")
print(f"A lista de pares é {valoresPares}")
print(f"A lista de ímpares é {valoresImpares}")
