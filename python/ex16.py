#Digite um numero real para ver sua porção inteira 
import math
numero = float(input('Digite um  valor para ver sua porção inteira: '))
por = math.trunc(numero)
print('A porção inteira de {} era {}.'.format(numero,por))