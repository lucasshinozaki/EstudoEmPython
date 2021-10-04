tupla = ("Coxinha", 3.00, "Lasanha", 25.00, "Coca-cola", 10.00, "Pizza", 30.00,
         "Pudim", 20.00, "Torta-limão", 35.00, "Esfiha", 5.00, "Pão de Queijo", 7.00)

print("-" * 54)
print(" " * 20, end=" ")
print("Asuna Comidas")
print("-" * 54)
soma = 0
for c in range(0, len(tupla)):
    if c == 0:
        print(f"{tupla[c]:.<40}", end="")
    elif c % 2 == 0:
        print(f"{tupla[c]:.<40}", end="")
    else:
        print(f" R$ {tupla[c]:.2f}")
        soma += tupla[c]

print(f"Soma", end="." * 36)
print(f" R$ {soma}")
