#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
#largura e comprimento e mostre a área do terreno

def area(a, b):
    print(f"A área de um terreno {a} x {b} é de {a * b}m²")


print('Controle de Terrenos')
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
