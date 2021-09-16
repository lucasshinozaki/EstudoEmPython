km = float(input('Digite o Km: '))

if km < 200:
    print('O preço a ser pago: R${:.2f}'.format(km * 0.50))
else:
    print('O preco a ser pago: R${:.2f}'.format(km * 0.45))

