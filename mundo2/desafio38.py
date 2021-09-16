n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

if n1 == n2:
    print('Nãoo existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O primeiro valor é maior: {}'.format(n1))
else:
    print('O segundo valor é o maior: {}'.format(n2))
