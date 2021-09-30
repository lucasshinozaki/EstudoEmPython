#Desafio 72
#Cire um programa que tenha uma tupla totalmente preenchido com uma contagem por extenso, de zero até vinte
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'tres', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input("Digite um número entre [0 e 20]"))
while num < 0 or num > 20:
    num = int(input("Tente novamente! Digite um número entre [0 e 20]"))

print(f'Voce digitou o numero: {numeros[num]}')

