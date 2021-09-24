#Desafio 67
#Faça um programa que mostre a tabuada de vários números
#Um de cada vez, para cada valor digitado pelo usuário
#O programa sera interrompido quando o número solicitado for negativo

while True:
    print("-=-" * 20)
    numero = int(input("Quer ver a tabuada de qual valor [negativo para sair]: "))
    if numero < 0:
        break;
    for c in range(0, 11):
        print(f"{numero} X {c} = {numero * c}")
print("TABUADA ENCERRADA. Volte sempre")


