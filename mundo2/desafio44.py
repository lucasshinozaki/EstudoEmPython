print('Menu: ')
print('[1] - Dinheiro/cheque')
print('[2] - Cartao')
print('[3] - 2x no cartão')
print('[4] - 3x no cartão')
forma = int(input('Digite uma entrada: '))
valor = float(input('Digite o valor: '))

if forma == 1:
    print('O valor vai ser: R${:.2f}'.format(valor - (valor * 0.1)))
elif forma == 2:
    print('O valor vai ser: R${:.2f}'.format(valor - (valor * 0.05)))
elif forma == 3:
    print('O valor vai ser: R${:.2f}'.format(valor))
    print('Sua compra será parcelada em 2x de R${:.2f}, sem juros'.format(valor/2))
elif forma == 4:
    contpar = int(input('Quantas parcelas: '))
    print('O valor vai ser: {:.2f}'.format((valor * 0.2) + valor))
    print('Sua compra sera parcelada em {}x de R${:.2f}'.format(contpar, ((valor * 0.2) + valor)/contpar))
else:
    print('Opção invalida!!, Tente novamente')
