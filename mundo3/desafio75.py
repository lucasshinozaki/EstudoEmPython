#Desafio 75
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9
#B) Em que posição foi digitado o primeiro valor 3
#C) Quais foram os números pares

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
tupla = (n1, n2, n3, n4)

print(f"Você digitou os valore {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")

verificar = tupla.count(3)
if verificar == 0:
    print("O valor 3 não foi digitado em nenhuma posição")
else:
    print(f"O valor 3 apareceu na {tupla.index(3) + 1} posição")

cont = cont2 = 0
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        cont2 += 1
        if cont2 == 1:
            print(f"Os valores pares digitados foram {tupla[c]}", end=", ")
        else:
            print(tupla[c], end=", ")
