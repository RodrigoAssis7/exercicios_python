#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
sa = float(input("qual o salario atual do funcionario: "))
aumento = sa * 15 / 100
no = sa + aumento
print("O salario atual do funcionario com 15% de aumento fica: R${}".format(no))