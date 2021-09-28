# Desafio 70
# Crie um programa que leia o nome e o preço de vários produtos
# O programa deverá perguntar se o usuário vai continuar
# No final, mostre:
#   A - Qual é o total gasto na compra
#   B - Quantos produtos custam mais de R$1000
#   C - Quel é o nome do produto mais barato
total = caro = menor = cont = nomeM = 0
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    print("-" * 30)
    opcao = input("Quer continuar? [S/N]: ").strip().upper()[0]
    print("-" * 30)
    while opcao not in 'SsNn':
        opcao = input("Quer continuar? [S/N]: ").strip().upper()[0]
    total += preco
    cont +=1
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomeM = nome
    if opcao == 'N':
        break

print(f"O total da compra foi R${total:.2f}")
print(f"Temos {caro} custando mais de R$1000.00")
print(f"O produto mmais barato foi {nomeM} que custa R${menor}")