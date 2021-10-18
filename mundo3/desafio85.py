#Desafio 85
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#Que mantenha separados os valores pares e ímpares. No final mostre os valores paraes e ímpares em ordem crescente

lista = list()
impar = list()
par = list()
for c in range (0, 7):
    valores = int(input(f"Digite o valor {c}o. valor: "))
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)

lista.append(par)
lista.append(impar)

print(lista)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares digiteados foram: {lista[0]}")
print(f"Os valores ímpares digitados forma {lista[1]}")
