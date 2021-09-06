
salario = float(input('Digite seu salario: '))

if salario > 1250:
    print('O seu aumento vai ser de: R${:.2f}\nO salario vai ser de: R${:.2f}'.format(salario * 0.10, (salario * 0.10 + salario)))

else:
    print('O seu aumento vai ser de: R${:.2f}\nO salario vai ser de: R${:.2f}'.format(salario * 0.15, (salario * 0.15 + salario)))
