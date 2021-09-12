#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#Desconsiderando os espaços

frase = str(input('Digite uma frase: '))

frasesem = "".join(frase.split())
fraseinvertida = frasesem[::-1]

print(frasesem)
print(fraseinvertida)

if frasesem == fraseinvertida:
    print("A frase é um palindromo ")
else:
    print("A frase não é um palindromo")
