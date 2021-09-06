valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite a quantidade de anos: '))

pres = valor / (anos * 12)

if (salario * 0.3) < pres:
    print('Voce não tem consições de pagar: \nprestação:{:.2f} por mes\nsalario:{:.2f} por mes'.format(pres, salario))
else:
    print('Voce tem consições de pagar: \nprestação:{:.2f} por mes\nsalario:{:.2f}'.format(pres, salario))
