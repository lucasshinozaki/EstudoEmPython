#Desafio 77
#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis",
            "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")


for c in range(0, len(palavras)):
    print(f"Na palavra {palavras[c]} temos ", end="")
    qtdDeA = palavras[c].count('a')
    qtdDeE = palavras[c].count('e')
    qtdDeI = palavras[c].count('i')
    qtdDeO = palavras[c].count('o')
    qtdDeU = palavras[c].count('u')
    if qtdDeA > 0:
        for a in range(0, qtdDeA):
            print(" a", end="")
    if qtdDeE > 0:
        for e in range(0, qtdDeE):
            print(" e", end="")
    if qtdDeI > 0:
        for e in range(0, qtdDeI):
            print(" i", end="")
    if qtdDeO > 0:
        for e in range(0, qtdDeO):
            print(" o", end="")
    if qtdDeU > 0:
        for e in range(0, qtdDeU):
            print(" u", end="")
    print(" ")
