n1 = float(input('Digite um lado: '))
n2 = float(input('Digite um lado: '))
n3 = float(input('Digite um lado: '))

if n3 < n1 + n2 and n2 < n1 + n3 and n1 < n2 + n3:
    print('Eh um triangulo')
else:
    print('Não eh um triangulo')
