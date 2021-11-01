#Desafio 97
#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetor e mostre
#Uma mensagem com tamanho adaptável

def escreva(msg):
    tam = len(msg)
    print("-" * tam)
    print(f"{msg}")
    print("-" * tam)


escreva("   Curso de Python no YouTube   ")
escreva("   Lucas Shinozaki   ")
escreva("   Lucas   ")
escreva("   CEV   ")