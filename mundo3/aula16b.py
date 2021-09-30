pessoa = ('Lucas', 22, 'M', 90.00)
#apagando tupla
del(pessoa)

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = b + a

print("Tamanho de c")
print(len(c))

print("Quantidade de 5 em a e b")
print(c.count(5))

print("Posição do 8")
print(c.index(8))
