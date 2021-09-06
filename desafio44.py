print('Menu: ')
print('1 - Dinheiro/cheque')
print('2 - Cartao')
print('3 - 2x no cartão')
print('4 - 3x no cartão')
forma = int(input('Digite uma entrada: '))
valor = float(input('Digite o valor: '))

if forma == 1:
    print('O valor vai ser: {:.2f}'.format(valor - (valor * 0.1)))
elif forma == 2:
    print('O valor vai ser: {:.2f}'.format(valor - (valor * 0.05)))
elif forma == 3:
    print('O valor vai ser: {:.2f}'.format(valor))
elif forma == 4:
    print('O valor vai ser: {:.2f}'.format((valor * 0.2) + valor))
