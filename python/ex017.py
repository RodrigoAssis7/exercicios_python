from math import sqrt

oposto = float(input("Digite o valor do cateto oposto: "))
adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = sqrt(oposto**2 + adjacente*2)

print("O valor da hipotenusa e {:.2f}".format(hipotenusa))