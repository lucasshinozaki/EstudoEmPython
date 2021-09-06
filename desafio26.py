frase = str(input('Digite uma frase : ')).strip()

print('Quanto vezes aparece a letra {}'.format(frase.count('a')).lower())
print('Aparece pela primeira vez {}'.format(frase.find('a')).lower())
print('Aparece pela ultima vez {}'.format(frase.rfind('a')).lower())
