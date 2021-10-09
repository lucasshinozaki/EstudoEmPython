#Desafio 78
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
#No final, mostre qual for o maior e o menor valor digitados e as suas respectivas posições na lista

valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
print("=-"*40)

print(f'Você digitou os valores {valores}')
print(f"O maior valor digitado foi {max(valores)} nas posições ", end="")
for c in range(0, len(valores)):
    if valores[c] == max(valores):
        print(f"{c}... ", end="")

print(f"\nO maior valor digitado foi {min(valores)} nas posições ", end="")
for c in range(0, len(valores)):
    if valores[c] == min(valores):
        print(f"{c}... ", end="")
