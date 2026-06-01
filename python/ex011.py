lar = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = lar * alt
tinta = area / 2
print("A area da parede sera: {:.2f}m²\nA Quantidade de tinta a ser usada sera: {:.2f}L".format(area, tinta))