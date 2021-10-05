#Desafio 77
#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis",
            "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")

vogais = ("a", "e", "i", "o", "u")

for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c]} temos ', end="")
    for d in range(0, len(vogais)):
        quantidade = palavras[c].count(vogais[d])
        for q in range(0, quantidade):
            print(vogais[d], end=" ")
    print("")