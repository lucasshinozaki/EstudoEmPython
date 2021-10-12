#Desafio 81
#Crei um programa que vai ler vários números e colocar em uma lista
#Depois disso, mostre:
#A) Quantos números foram digitados
#B) A lista de valores, ordenado de forma descrescente
#C) Se o valor 5 for digitado e está ou não na lista

opcao = ""
valores = list()
cont = 0
while opcao != "N":
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()

print(f"Você digitou {cont} elementos")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if valores.count(5) > 0:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista")