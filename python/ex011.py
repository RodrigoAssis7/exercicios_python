#Faça um programa que leia a largura e a altura de um parede em metros e calcule sua área e a quantidade de tinta
# necessária para pintala, sabendo que cada litro de tinta pinta uma área de 2mQ
lar = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = lar * alt
tinta = area / 2
print("A area da parede sera: {:.2f}m²\nA Quantidade de tinta a ser usada sera: {:.2f}L".format(area, tinta))