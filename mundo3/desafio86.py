#Desafio 86
#Crie um programa que crie uma matrix de dimensão 3X3 e preencha com valores lidos pelo teclado
#No final mostre a matriz na tela, com formatação correta
lista = list()
dados = list()

for i in range(0,3):
    for j in range(0,3):
        dados.append(int(input(f"Digite um valor para [{i}, {j}]: ")))
    lista.append(dados[:])
    dados.clear()

for c in range(0, 3):
    print(lista[c])
