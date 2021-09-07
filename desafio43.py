peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc > 40:
    print('Obesidade Mórbida, IMC: {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade, IMC: {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso, IMC:{:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Ideal, IMC: {:.2f}'.format(imc))
else:
    print('Abaixo do Peso, IMC: {:.2f}'.format(imc))
