#Desafio 79
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o números já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = []
opcao = ""
cont = 0
while opcao != "N":
    aux = int(input("Digite um valor: "))
    for aux in valores:
        print("Valor duplicado! Não vou adicionar...")
        cont += 1
    if cont == 0:
        print("Valor adicionado com sucesso...")
        valores.append(aux)
    cont = 0
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()

valores.sort()
print(f"Você digitou os valores {valores}")
