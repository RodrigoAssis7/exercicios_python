#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar . Considere = R$3,27
con = float(input("Digite quanto voçê tem na carteira: "))
dol = con / 3.27
print("O valor que voçê podera comprar com R${:.2f} e U${:.2f}".format(con,dol))