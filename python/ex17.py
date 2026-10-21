#Programa que lei ao cateto oposto e o cateto adjaçente  emostre a hipotenuza 
import math
ad = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do cateto oposto: '))

hipotenuza = math.sqrt (ad**2 + op**2)

print('O valor da hipotenuza sera {:.2f}.'.format(hipotenuza))