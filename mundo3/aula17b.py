#lista

a = [2, 3, 4, 7]
# Igualando uma lista
b = a
# Criando uma copia de a
c = a[:]
c[2] = 6
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista C: {c}")

#Adicionando varios valores para uma lista
valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))

#Adicionando valores a uma lista
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#Imprimindo os valores de uma lista de forma separada
for valor in valores:
    print(f"{valor} ", end="")
print("")

#Imprimindo a lista de forma enumerada
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
