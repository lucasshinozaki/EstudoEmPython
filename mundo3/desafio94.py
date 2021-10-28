# Desafio 94
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario
# e todos os dicionarios em uma lista, No final mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessocas com idade acima da média

dicionario = dict()
lista = list()

total = 0
while True:
    dicionario['nome'] = str(input("Nome: ")).strip().title()
    dicionario['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()
    while dicionario['sexo'] not in "MF":
        dicionario['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()
    dicionario['idade'] = int(input("Idade: "))
    total += dicionario['idade']
    lista.append(dicionario.copy())
    opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    while opcao not in "NS":
        opcao = input("Quer continuar ? [S/N]: ").strip().upper()
    if opcao == 'N':
        break

print("-=" * 30)
print(f"->O grupo tem {len(lista)} pessoas")
print(f"->A média de idade é de {total/len(lista):.2f}")
print("->As mulheres cadastradas foram: ", end=" ")

for dados in lista:
    for k, v in dados.items():
        if k == "sexo" and v == "F":
            print(dados['nome'], end=" ")

print("\n->Lista das pessoas que estão acima da média:")
for dados in lista:
    print()
    for k, v in dados.items():
        if dados['idade'] > total/len(lista):
            print(k, v, end="; ")

print("<< ENCERADOO >>")