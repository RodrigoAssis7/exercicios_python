#Faça um algoritmo que leia o preço de um produto e mostre o seu preço com desconto de 5%
pro = float(input("Digite o valor do produto: "))
des = pro - (pro * 5 / 100)
print("O valor com desconto de 5% sera {}".format(des))