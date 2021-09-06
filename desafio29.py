num = int(input('Digite a velocidade: '))

if num > 80:
    print('Vc foi MULTADO no valor de R$ {:.2f}'.format((num - 80) * 7))
else:
    print('Vc não foi multado')
