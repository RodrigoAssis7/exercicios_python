#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o nome da pessoa: ')).strip()
print('O nome da pessoa tem "SILVA"? {}'.format('SILVA' in nome.upper()))