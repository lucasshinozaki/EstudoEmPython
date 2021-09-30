#Tuplas

lanche = ('Hamburque', 'Suco', 'Pizza', 'Pudim')
print(lanche[::-1])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Posição {pos} Eu vou comer {comida}')

print(sorted(lanche))

print('Comi pra caramba !!!')
