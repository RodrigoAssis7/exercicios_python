#Crie um algoritmo que leia um número e mostre o seu dobro , triplo e raiz quadrada
numero = int(input('Digite um valor: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print('o dobro de {} sera: {} \nseu tripo sera: {} \nsua raiz quadrada: {}.'.format(numero, dobro, triplo, raiz_quadrada))