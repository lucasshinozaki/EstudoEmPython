# Desafio 84
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Um listagem com as pessoas mais leves

pessoa = list()
dado = list()
opcao = ''
cont1 = cont2 = maior = menor = 0
while opcao != 'N':
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    dado.append(pessoa[:])
    pessoa.clear()
    cont1 += 1
    for p in dado:
        cont2 += 1
        if cont2 == 1:
            maior = p[1]
            menor = p[1]
        else:
            if p[1] > maior:
                maior = p[1]
            elif p[1] < menor:
                menor = p[1]
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()

print(f"Ao todo, você cadastrou {cont1} pessoa.")
print(f"O maior peso foi de {maior}Kg. Peso de", end=" ")
for p in dado:
    if p[1] == maior:
        print(p[0], end=" ")
print(f"\nO menor peso foi de {menor}Kg. Peso de", end=" ")
for p in dado:
    if p[1] == menor:
        print(p[0], end=" ")