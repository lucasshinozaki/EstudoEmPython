# Desafio 99
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*valores):
    print("Analisando os valores passados...")
    for num in valores:
        print(f"{num}", end=" ")
    print(f"Foram informados {len(valores)} ao todo;")
    if len(valores) == 0:
        print(f"O maior valor informado foi 0")
    else:
        print(f"O maior valor informado foi {max(valores)}")
    print("--" * 20)


print("--" * 20)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7 , 0)
maior(1, 2)
maior(6)
maior()
