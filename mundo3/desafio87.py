# Desafio 87
# Aprimore o desafio anterior, mostrando no final
# A)A soma de todos os valores pares digitados
# B)A soma dos valores da terceira coluna
# C)O maior valor da segunda linha

lista = list()
dados = list()

for i in range(0, 3):
    for j in range(0, 3):
        dados.append(int(input(f"Digite um valor para [{i}, {j}]: ")))
    lista.append(dados[:])
    dados.clear()

for c in range(0, 3):
    print(lista[c])

pares = colTres = 0
for valores in lista:
    for valor in valores:
        if valor % 2 == 0:
            pares += valor
    colTres += valores[2]

print("--" * 30)
print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da terceira coluna é  {colTres}")
print(f"O maior valor da segunda linha é {max(lista[1])}")
