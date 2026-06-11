import math

angulo = float(input("Digite o valor do angulo: "))
red = math.radians(angulo)

seno = math.sin(red)
cosseno = math.cos(red)
tangente = math.tan(red)

print('seno do angulo {:.3f}'.format(seno))
print('cosseno do angulo {:.3f}'.format(cosseno))
print('tangente do angulo {:.3f}'.format(tangente))