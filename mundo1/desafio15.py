km = int(input('Km percorridos : '))
dias = int(input('Quantidade de dia : '))

preco_km = km * 0.15
preco_dias = dias * 60
custo = preco_km + preco_dias
print('O total a pagar eh : {:.2f}'. format(custo))